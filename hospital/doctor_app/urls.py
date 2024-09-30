from django.urls import path
from .views import create_doctor,DoctorRegistration,doctor_list,Doctor_login
urlpatterns = [
    path('doctor_create/',create_doctor,name='doctor_create'),
    path('doctor_list/',doctor_list,name='doctor_list'),
    path('',DoctorRegistration,name='doctor_register'),
    path('doctor_login',Doctor_login,name='doctor_login'),
]