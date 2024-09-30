from django import forms
from .models import DoctorCreate
from django import forms

class CreateDoctorForm(forms.ModelForm):
    class Meta:
        model = DoctorCreate
        fields = '__all__'




