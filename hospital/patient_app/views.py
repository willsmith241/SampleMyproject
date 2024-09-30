import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from django.urls import reverse


from django.contrib.auth import authenticate, login

from .models import BookAppointment,LoginTable,UserProfile
from .forms import BookAppointmentForm
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

from doctor_app.models import DoctorCreate





def appointment_list(request):
    bookings = BookAppointment.objects.all()

    return render(request,'patient/booking_list.html',{'bookings':bookings})

def appointment_book(request):
    if request.method == 'POST':
        form = BookAppointmentForm(request.POST)
        print(form)

        if form.is_valid():
            appointment = form.save()
            return redirect('stripe_payment', id=appointment.id)

    else:
        form = BookAppointmentForm()

    return render(request,'patient/booking.html',{'form':form})


def stripe_payment(request,id):
    appointment = BookAppointment.objects.get(id=id)

    if request.method == 'POST':
        # Create a Stripe session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'INR',
                        'product_data': {
                            'name': f"Appointment with {BookAppointment.patient_name}",
                        },
                        'unit_amount': 5000,  # Amount in cents ($50.00)
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),  # Use reverse here
            cancel_url=request.build_absolute_uri(reverse('cancel')),

        )
        return redirect(session.url, code=303)


    return render(request, 'patient/payment.html', {'appointment': appointment})


def success(request):
    return render(request, 'patient/success_url.html')


def cancel(request):
    return render(request, 'patient/cancel.html')


def booking_details(request, appointment_id):
    appointment = BookAppointment.objects.get (id=appointment_id)



    return render(request, 'patient/booking_details.html', {'appointment': appointment})






def UserRegistration(request):

    login_table= LoginTable()
    userprofile=UserProfile()

    if request.method=='POST':
        userprofile.username=request.POST['username']
        userprofile.password = request.POST['password']
        userprofile.password1 = request.POST['password1']

        login_table.username=request.POST['username']
        login_table.password = request.POST['password']
        login_table.password1 = request.POST['password1']
        login_table.type = 'user'

        if request.POST['password']==request.POST['password1']:
            userprofile.save()
            login_table.save()

            messages.info(request,'Registration Success Fully')
            return redirect('login')

        else:
            messages.info(request,'Password not matching')
            return redirect('register')

    return render(request,'patient/patient_register.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=LoginTable.objects.filter(username=username,password=password,type='user').exists()

        try:
            if user is not None:
                user_details=LoginTable.objects.get(username=username,password=password)
                user_name=user_details.username
                type=user_details.type

                if type == 'user':
                    request.session['username'] = user_name
                    return redirect('doctor_book_list')
                elif type == 'admin':
                     request.session['username'] = user_name
                     return redirect('doctor_book_list')
            else:
                messages.error(request,'invalid  user name or password')

        except:
            messages.error(request,'invalid role')

    return render(request,'patient/patient_login.html')

def doctor_book_list(request):
    doctors = DoctorCreate.objects.all()

    return render(request,'patient/doctor_book.html',{'doctors':doctors})


