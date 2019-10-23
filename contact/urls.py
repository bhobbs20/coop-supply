from django.urls import path

from . import views

urlpatterns = [
    
    path('contact_coupsupply', views.contact_coupsupply, name='contact_coupsupply')
]