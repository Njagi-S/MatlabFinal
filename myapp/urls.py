from django.contrib import admin  # Import the admin module for accessing the Django admin panel.
from django.urls import path  # Import the path function to define URL patterns.
from myapp import views  # Import the views from the 'myapp' application.

# URL patterns define the mapping between URLs and their corresponding views.
urlpatterns = [
    # Admin site URL.
    path('admin/', admin.site.urls),  # Access the Django admin interface.

    # URL for the index page.
    path('index/', views.index, name='index'),  # Calls the `index` view, named 'index' for easy reference.

    # URL for the service page.
    path('service/', views.service, name='service'),  # Calls the `service` view, named 'service'.

    # URL for the starter page.
    path('starter/', views.starter, name='starter'),  # Calls the `starter` view, named 'starter'.

    # URL for the about page.
    path('about/', views.about, name='about'),  # Calls the `about` view, named 'about'.

    # URL for the services overview page.
    path('myservice/', views.myservice, name='myservice'),  # Calls the `myservice` view, named 'myservice'.

    # URL for the doctors page.
    path('doctors/', views.doctors, name='doctors'),  # Calls the `doctors` view, named 'doctors'.

    # URL for the departments page.
    path('departments/', views.departments, name='departments'),  # Calls the `departments` view, named 'departments'.

    # URL for the contacts page (for submitting or viewing the contact form).
    path('contacts/', views.contacts, name='contacts'),  # Calls the `contacts` view, named 'contacts'.

    # URL for scheduling an appointment.
    path('appointment/', views.appointment, name='appointment'),  # Calls the `appointment` view, named 'appointment'.

    # URL to show all appointments.
    path('show/', views.show, name='show'),  # Calls the `show` view to display all appointments, named 'show'.

    # URL to delete an appointment (with the appointment ID as a parameter).
    path('delete/<int:id>', views.delete),  # Calls the `delete` view, deleting the appointment by its ID.

    # URL to show all contact inquiries.
    path('showcontacts/', views.showcontacts, name='showcontacts'),  # Calls the `showcontacts` view, named 'showcontacts'.

    # URL to delete a contact inquiry (with the contact ID as a parameter).
    path('deletecontacts/<int:id>', views.deletecontacts),  # Calls the `deletecontacts` view, deleting a contact by its ID.

    # URL to edit an appointment (with the appointment ID as a parameter).
    path('edit/<int:id>', views.edit, name='edit'),  # Calls the `edit` view to edit the appointment, named 'edit'.

    # URL to update an appointment (with the appointment ID as a parameter).
    path('update/<int:id>', views.update, name='update'),  # Calls the `update` view to save edited appointment details, named 'update'.

    # URL to edit a contact inquiry (with the contact ID as a parameter).
    path('editcontacts/<int:id>', views.editcontacts, name='editcontacts'),  # Calls the `editcontacts` view, named 'editcontacts'.

    # URL to update a contact inquiry (with the contact ID as a parameter).
    path('updatecontacts/<int:id>', views.updatecontacts, name='updatecontacts'),  # Calls the `updatecontacts` view, named 'updatecontacts'.

    # URL for the registration page (default landing page).
    path('', views.register, name='register'),  # Calls the `register` view, which is the default route, named 'register'.

    # URL for the login page.
    path('login/', views.login, name='login'),  # Calls the `login` view, named 'login'.

    # URL pattern for the image upload page.
    path('uploadimage/', views.upload_image, name='upload'),  
    # Maps the '/uploadimage/' URL to the `upload_image` view function.
    # The name 'upload' allows you to reference this URL easily in templates or code.
    # This route enables users to upload images using a form.

    # URL pattern for displaying all uploaded images.
    path('showimage/', views.show_image, name='image'),  
    # Maps the '/showimage/' URL to the `show_image` view function.
    # The name 'image' is used to refer to this URL in templates or for reverse lookups.
    # This route allows users to view a list or gallery of uploaded images.

    # URL pattern for deleting a specific image by its ID.
    path('imagedelete/<int:id>', views.imagedelete),  
    # Maps the '/imagedelete/<int:id>' URL to the `imagedelete` view function.
    # Captures the integer `id` from the URL and passes it as a parameter to the view.
    # This route enables the deletion of an image record identified by its unique ID.

]
