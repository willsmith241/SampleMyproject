from django import forms
from django.contrib.auth.models import User

from .models import BookAppointment,UserProfile




class BookAppointmentForm(forms.Form):
    appointment_type = forms.ChoiceField(choices=[
        ('general', 'General Consultation'),
        ('specialist', 'Specialist Consultation'),
        # Add more types as needed
    ])
class BookAppointmentForm(forms.ModelForm):
     class Meta:
         model = BookAppointment

         fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
