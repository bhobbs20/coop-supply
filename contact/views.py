from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact_coupsupply(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    
    contact = Contact(name=name, email=email, subject=subject, message=message)

    contact.save()
    messages.success(request, 'Thank you for contacting Coup Supply, a staff member will get back to you soon')
  
    return redirect('index')




    


