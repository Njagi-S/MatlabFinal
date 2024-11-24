from django import forms
from myapp.models import Appointment, Contacts, ImageModel

# Define a form for managing Appointment data
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment  # Link this form to the Appointment model
        fields = '__all__'   # Include all fields from the Appointment model
        # This allows automatic generation of form fields based on the Appointment model.

# Define a form for managing Contacts data
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts  # Link this form to the Contacts model
        fields = '__all__'  # Include all fields from the Contacts model
        # Useful for capturing contact details like name, email, subject, and message.

# Define a form for uploading images
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel  # Link this form to the ImageModel
        fields = ['image', 'title', 'price']  # Specify the fields to include in the form
        # This form will allow users to upload an image file, set a title, and provide a price.
