import json

import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

from django.shortcuts import render, redirect
from myapp.credentials import MpesaAccessToken, LipanaMpesaPassword
from myapp.models import Appointment, Contacts, Member, ImageModel
from myapp.forms import AppointmentForm, ContactForm, ImageUploadForm

# The main index view: handles user login
def index(request):
    if request.method == 'POST':  # If the request is POST, process login credentials
        # Check if a member with provided username and password exists
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password'],
        ).exists():
            # Fetch the member details
            members = Member.objects.get(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            # Render the index page if login is successful
            return render(request, 'index.html', {'members': members})
        else:
            # Redirect back to the login page if credentials are invalid
            return render(request, 'login.html')
    else:
        # Render the login page for GET requests
        return render(request, 'login.html')

# Renders the service details page
def service(request):
    return render(request, 'service-details.html')

# Renders the starter page
def starter(request):
    return render(request, 'starter-page.html')

# Renders the about page
def about(request):
    return render(request, 'about.html')

# Renders the services page
def myservice(request):
    return render(request, 'services.html')

# Renders the doctors page
def doctors(request):
    return render(request, 'doctors.html')

# Renders the departments page
def departments(request):
    return render(request, 'departments.html')

# Handles contact form submissions and displays the contacts page
def contacts(request):
    if request.method == 'POST':  # Process the form if it's a POST request
        mycontacts = Contacts(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontacts.save()  # Save the contact information to the database
        return redirect('/showcontacts')  # Redirect to the list of contacts
    else:
        return render(request, 'contacts.html')  # Render the contacts page for GET requests

# Handles appointment form submissions and displays the appointment page
def appointment(request):
    if request.method == 'POST':  # Process the form if it's a POST request
        myappointment = Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
        myappointment.save()  # Save the appointment to the database
        return redirect('/show')  # Redirect to the list of appointments
    else:
        return render(request, 'appointment.html')  # Render the appointment page for GET requests

# Displays all appointments
def show(request):
    allappointments = Appointment.objects.all()  # Fetch all appointments
    return render(request, 'show.html', {'appointment': allappointments})

# Deletes an appointment based on its ID
def delete(request, id):
    appoint = Appointment.objects.get(id=id)  # Fetch the appointment by ID
    appoint.delete()  # Delete the appointment
    return redirect('/show')  # Redirect to the list of appointments

# Displays all contact submissions
def showcontacts(request):
    allcontacts = Contacts.objects.all()  # Fetch all contacts
    return render(request, 'showcontacts.html', {'contact': allcontacts})

# Deletes a contact submission based on its ID
def deletecontacts(request, id):
    mycontacts = Contacts.objects.get(id=id)  # Fetch the contact by ID
    mycontacts.delete()  # Delete the contact
    return redirect('/showcontacts')  # Redirect to the list of contacts

# Displays a form for editing an appointment and processes updates
def edit(request, id):
    editappointment = Appointment.objects.get(id=id)  # Fetch the appointment by ID
    return render(request, 'edit.html', {"appointment": editappointment})

def update(request, id):
    updateinfo = Appointment.objects.get(id=id)  # Fetch the appointment by ID
    form = AppointmentForm(request.POST, instance=updateinfo)  # Bind data to the form
    if form.is_valid():  # Validate the form
        form.save()  # Save the updates
        return redirect('/show')  # Redirect to the list of appointments
    else:
        return render(request, 'edit.html')  # Reload the edit page if validation fails

# Displays a form for editing a contact and processes updates
def editcontacts(request, id):
    editcontact = Contacts.objects.get(id=id)  # Fetch the contact by ID
    return render(request, 'editcontacts.html', {"contact": editcontact})

def updatecontacts(request, id):
    updatecontactsinfo = Contacts.objects.get(id=id)  # Fetch the contact by ID
    form = ContactForm(request.POST, instance=updatecontactsinfo)  # Bind data to the form
    if form.is_valid():  # Validate the form
        form.save()  # Save the updates
        return redirect('/showcontacts')  # Redirect to the list of contacts
    else:
        return render(request, 'editcontacts.html')  # Reload the edit page if validation fails

# Handles user registration
def register(request):
    if request.method == 'POST':  # Process registration form if it's a POST request
        members = Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        members.save()  # Save the new member to the database
        return redirect('/login')  # Redirect to the login page
    else:
        return render(request, 'register.html')  # Render the registration page for GET requests

# Renders the login page
def login(request):
    return render(request, 'login.html')

# Function to handle image upload
def upload_image(request):
    # Check if the HTTP method is POST (indicates form submission).
    if request.method == 'POST':
        # Create an instance of the ImageUploadForm, populated with the submitted data and files.
        form = ImageUploadForm(request.POST, request.FILES)
        # Validate the form inputs.
        if form.is_valid():
            form.save()  # Save the valid form data into the database.
            return redirect('/showimage')  # Redirect to the 'showimage' page after a successful upload.
    else:
        # If the request method is GET, create a blank form instance.
        form = ImageUploadForm()
    # Render the 'upload_image.html' template with the form for the user to fill.
    return render(request, 'upload_image.html', {'form': form})

# Function to display all uploaded images
def show_image(request):
    # Query all image records from the database.
    images = ImageModel.objects.all()
    # Render the 'show_image.html' template, passing the retrieved images to the context.
    return render(request, 'show_image.html', {'images': images})

# Function to delete an uploaded image by its ID
def imagedelete(request, id):
    # Retrieve the image object from the database using the provided ID.
    image = ImageModel.objects.get(id=id)
    # Delete the retrieved image object from the database.
    image.delete()
    # Redirect to the 'showimage' page after successful deletion.
    return redirect('/showimage')

def token(request):
    consumer_key = '8mS9cYpGqSB4gMRew6aBdpdtP6DoToa8rb6XmExn6lGLigug'
    consumer_secret = 'Ds2p7VX7uDXoObc8jK2NRrhZk6QGK9BhKhvFA08WVg8g3MBwF55u9TlDckSxWKyj'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
    return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")