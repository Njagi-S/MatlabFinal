from django import forms
from myapp.models import Appointment, Contacts


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'

