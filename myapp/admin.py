from django.contrib import admin
from myapp.models import Student, Product ,Patient, Appointment, Contacts

# Register your models here.
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Contacts)