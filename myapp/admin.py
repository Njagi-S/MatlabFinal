from django.contrib import admin  # Import the admin module for managing models via the Django admin interface
from myapp.models import Student, Product, Patient, Appointment, Contacts, Member, ImageModel

# Register your models here.

# Register the Student model with the admin site.
# This allows the admin user to view, add, edit, and delete Student objects through the Django admin interface.
admin.site.register(Student)

# Register the Product model with the admin site.
# This enables admin users to manage Product entries via the admin interface.
admin.site.register(Product)

# Register the Patient model with the admin site.
# Admin users can now manage Patient information through the admin interface.
admin.site.register(Patient)

# Register the Appointment model with the admin site.
# This allows appointments to be managed directly from the Django admin interface.
admin.site.register(Appointment)

# Register the Contacts model with the admin site.
# This enables admin users to handle contact submissions, such as inquiries, via the admin interface.
admin.site.register(Contacts)

# Register the Member model with the admin site.
# Admin users can add, edit, and delete Member accounts directly from the admin interface.
admin.site.register(Member)

# Register the ImageModel with the admin site.
# This allows managing ImageModel records directly from the Django admin panel
admin.site.register(ImageModel)
