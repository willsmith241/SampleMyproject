from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from .forms import CreateDoctorForm
from .models import DoctorCreate,RegisterDoctor,DoctorLoginTable
from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth import authenticate, login



# Create your views here.

def create_doctor(request):
    if request.method =='POST':

        form = CreateDoctorForm(request.POST,files=request.FILES)
        print(form)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = CreateDoctorForm()
    return render(request,'doctor/create_doctor.html',{'form':form})

def doctor_list(request):
    doctors = DoctorCreate.objects.all()


    return render(request,'doctor/doctor_list.html',{'doctors':doctors})



def DoctorRegistration(request):

    login_table= DoctorLoginTable()
    userprofile=RegisterDoctor()

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
            return redirect('doctor_login')

        else:
            messages.info(request,'Password not matching')
            return redirect('register')

    return render(request,'doctor/doctor_register.html')

def Doctor_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=DoctorLoginTable.objects.filter(username=username,password=password,type='user').exists()

        try:
            if user is not None:
                user_details=DoctorLoginTable.objects.get(username=username,password=password)
                user_name=user_details.username
                type=user_details.type

                if type == 'user':
                    request.session['username'] = user_name
                    return redirect('doctor_create')
                elif type == 'admin':
                     request.session['username'] = user_name
                     return redirect('doctor_create')
            else:
                messages.error(request,'invalid  user name or password')

        except:
            messages.error(request,'invalid role')

    return render(request,'doctor/doctor_login.html')











