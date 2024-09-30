from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import AdminLoginForm
from doctor_app.models import RegisterDoctor,DoctorCreate
# Create your views here.
from patient_app.models import UserProfile,BookAppointment
from django.shortcuts import render, redirect, get_object_or_404
from .models import AdminLoginTable,Admin_register

def booking_list(request):
    bookings = BookAppointment.objects.all()

    return render(request,'admin/appointment_list.html',{'bookings':bookings})

def delete_appointment(request,id):
    appointment = BookAppointment.objects.get(id=id)
    if request.method == "POST":
        appointment.delete()

        return redirect('dashboard')
    return render(request,'admin/appointment_delete.html')
def admin_dashboard(request):
    total_doctors = DoctorCreate.objects.count()  # Count total doctors
    total_patients = UserProfile.objects.count()
    total_bookings = BookAppointment.objects.count()# Count total patients

    return render(request, 'admin/dashboard.html', {
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_bookings':total_bookings,
    })

def home(request):

    return render(request,'home.html')

def AdminRegistration(request):

    login_table= AdminLoginTable()
    userprofile=Admin_register()

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
            return redirect('admin_login')

        else:
            messages.info(request,'Password not matching')
            return redirect('register')

    return render(request,'admin/admin_register.html')

def admin_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=AdminLoginTable.objects.filter(username=username,password=password,type='user').exists()

        try:
            if user is not None:
                user_details=AdminLoginTable.objects.get(username=username,password=password)
                user_name=user_details.username
                type=user_details.type

                if type == 'user':
                    request.session['username'] = user_name
                    return redirect('dashboard')
                elif type == 'admin':
                     request.session['username'] = user_name
                     return redirect('dashboard')
            else:
                messages.error(request,'invalid  user name or password')

        except:
            messages.error(request,'invalid role')

    return render(request,'admin/admin_login.html')


def doctor_list(request):
   doctors = DoctorCreate.objects.all()

   return render(request,'admin/doctor_list.html',{'doctors':doctors})

def patient_list(request):
    patients = UserProfile.objects.all()

    return render(request,'admin/patient_list.html',{'patients':patients})

def doc_register_list(request):
    doctors_page = DoctorCreate.objects.all()

    return render(request,'admin/doctor_register_list.html')


def delete_doctor(request,doc_id):

    doctor=DoctorCreate.objects.get(id=doc_id)

    if request.method=="POST":

        doctor.delete()

        return redirect('dashboard')

    return render(request,'admin/doctor_delete.html',{'doctor':doctor})

def patient_delete(request,id):
    patient = UserProfile.objects.get(id=id)

    if request.method == "POST":
        patient.delete()

        return redirect('dashboard')

    return render(request,'admin/patient_delete.html',{'patient':patient})

