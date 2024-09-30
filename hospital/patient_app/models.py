from django.db import models

# Create your models here.

class BookAppointment(models.Model):
    patient_name = models.CharField(max_length=200)
    patient_place =models.CharField(max_length=200)
    patient_phone = models.CharField(max_length=200)
    patient_dicese = models.CharField(max_length=200)
    how_meny_day_start_your_dicese =models.CharField(max_length=200)

    def __str__(self):
        return self.patient_name

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)

    def __str__(self):
        return '{}', format(self.username)

class LoginTable(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)

    type=models.CharField(max_length=50)

    def __str__(self):
        return '{}',format(self.username)


