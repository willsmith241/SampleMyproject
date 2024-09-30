
from django.db import models
# Create your models here.
class DoctorCreate(models.Model):
    doc_name = models.CharField(max_length=200)
    doc_img = models.ImageField(upload_to='media/')
    doc_phone = models.IntegerField()
    license_number = models.IntegerField()

    def __str__(self):
        return self.doc_name

class RegisterDoctor(models.Model):
    username = models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)

    def __str__(self):
        return '{}', format(self.username)

class DoctorLoginTable(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)

    type=models.CharField(max_length=50)

    def __str__(self):
        return '{}',format(self.username)