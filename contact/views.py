from django.shortcuts import render
from django.contrib import messages

from .models import Contact


def contact(request):
    template = 'contact/contact.html'
    context = {
        'contact_requests': Contact.objects.all().order_by('-created_on'),
    }

    return render(request, template, context)