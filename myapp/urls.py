
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('myservice/', views.myservice, name='myservice'),
    path('doctors/', views.doctors, name='doctors'),
    path('departments/', views.departments, name='departments'),
    path('contacts/', views.contacts, name='contacts'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('showcontacts/', views.showcontacts, name='showcontacts'),
    path('deletecontacts/<int:id>', views.deletecontacts),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('editcontacts/<int:id>', views.editcontacts, name='editcontacts'),
    path('updatecontacts/<int:id>', views.updatecontacts, name='updatecontacts'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
]
