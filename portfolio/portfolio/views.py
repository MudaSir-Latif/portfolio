
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings



def simple_view(request):
    return render(request, 'layout.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f"Contact Form Submission from {name}"
        full_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,  
            [settings.CONTACT_RECEIVER_EMAIL],  # recipient (your email)
            fail_silently=False,
        )
        return render(request, 'layout.html', {'success': True})
    return render(request, 'layout.html')
    

