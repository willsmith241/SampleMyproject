from django.db import models

# Create your models here.

class Admin_register(models.Model):
    username = models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)

    def __str__(self):
        return '{}', format(self.username)

class AdminLoginTable(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)

    type=models.CharField(max_length=50)

    def __str__(self):
        return '{}',format(self.username)