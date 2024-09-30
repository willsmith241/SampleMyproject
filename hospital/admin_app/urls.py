from django.urls import path
from .views import *
urlpatterns = [
    path('appointment_delete/<int:id>',delete_appointment,name='delete_appointment'),
    path('booking_list',booking_list,name='booking_list'),
    path('patient_delete/<int:id>',patient_delete,name='patient_delete'),
    path('delete_doctor/<int:doc_id>/',delete_doctor,name='delete_doctor'),
    path('dashboard',admin_dashboard,name='dashboard'),
    path('register_list/',doc_register_list,name='register_list'),
    path('',home,name='home'),
    path('admin_register/',AdminRegistration,name='admin_register'),
    path('admin_login/',admin_login,name='admin_login'),
    path('doctor_list/',doctor_list,name='doctor_register_list'),
    path('patient_list/',patient_list,name='patient_list')



]