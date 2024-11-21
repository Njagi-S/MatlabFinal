from django.db import models  # Import Django's ORM for creating and managing database models.

# Create your models here.

# Model for Student details
class Student(models.Model):
    fullname = models.CharField(max_length=100)  # Full name of the student, max 100 characters.
    username = models.CharField(max_length=100)  # Username for the student, max 100 characters.
    email = models.EmailField()  # Email field ensures valid email format.
    password = models.CharField(max_length=64)  # Password, max 64 characters (hashed or plain text).
    age = models.IntegerField()  # Integer field to store the student's age.
    yob = models.DateField()  # Date of Birth (Year of Birth) as a date field.

    def __str__(self):
        return self.fullname  # Returns the student's full name when the object is printed.

# Model for Product details
class Product(models.Model):
    name = models.CharField(max_length=100)  # Name of the product, max 100 characters.
    price = models.CharField(max_length=50)  # Price stored as a string (consider using DecimalField for better precision).
    quantity = models.IntegerField()  # Quantity of the product in stock.

    def __str__(self):
        return self.name  # Returns the product name when the object is printed.

# Model for Patient details
class Patient(models.Model):
    firstname = models.CharField(max_length=100)  # Patient's first name, max 100 characters.
    lastname = models.CharField(max_length=100)  # Patient's last name, max 100 characters.
    dateofbirth = models.DateField()  # Date of Birth of the patient.
    gender = models.CharField(max_length=100)  # Gender, stored as a string.
    email = models.EmailField()  # Email address of the patient.
    phonenumber = models.CharField(max_length=100)  # Phone number of the patient.
    address = models.CharField(max_length=100)  # Address of the patient.

    def __str__(self):
        return self.firstname  # Returns the first name when the object is printed.

# Model for Appointment details
class Appointment(models.Model):
    name = models.CharField(max_length=100)  # Name of the person making the appointment.
    email = models.EmailField()  # Email address for the appointment.
    phone = models.CharField(max_length=20)  # Phone number for the appointment.
    date = models.DateTimeField()  # Date and time of the appointment.
    department = models.CharField(max_length=50)  # Department the appointment is with.
    doctor = models.CharField(max_length=50)  # Doctor the appointment is scheduled with.
    message = models.TextField()  # Additional details or message for the appointment.

    def __str__(self):
        return self.name  # Returns the name of the person when the object is printed.

# Model for Contact submissions
class Contacts(models.Model):
    name = models.CharField(max_length=100)  # Name of the person submitting the contact form.
    email = models.EmailField()  # Email address for contact purposes.
    subject = models.CharField(max_length=50)  # Subject of the contact inquiry.
    message = models.TextField()  # Message content.

    def __str__(self):
        return self.name  # Returns the name of the person when the object is printed.

# Model for Member details (e.g., registered users)
class Member(models.Model):
    name = models.CharField(max_length=100)  # Full name of the member.
    username = models.CharField(max_length=100)  # Username for the member.
    password = models.CharField(max_length=64)  # Password, typically hashed.

    def __str__(self):
        return self.name  # Returns the name of the member when the object is printed.
