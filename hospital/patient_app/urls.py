from django.urls import path
from .views import *


urlpatterns = [
    path('doctor_book/',doctor_book_list,name='doctor_book_list'),
    path('login',LoginPage,name='login'),
    path('register/',UserRegistration,name='patent_register'),
    path('appointment_book',appointment_book,name='appointment_book'),
    path('appointment_list',appointment_list,name='booking_list'),
    path('payment/<int:id>/', stripe_payment, name='stripe_payment'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('booking_details/<int:appointment_id>/', booking_details, name='booking_details'),


]

