from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User

from profiles.models import UserProfile
from .models import Contact
from .forms import ContactForm


def contact(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
    else:
        user = None

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()
            contact.user = user
            contact.save()

            messages.success(request, "Message successfully sent. We will " +
                             "be in touch shortly via email with a " +
                             "response. Thank You.")
            return redirect(reverse('contact'))
        else:
            messages.error(request, "You didn't complete all of the required" +
                           " fields, please complete the form again.")

    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                form = ContactForm(initial={
                    'name': profile.user.get_full_name(),
                    'email': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                form = ContactForm()
        else:
            form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_requests': Contact.objects.all().order_by('-created_on'),
        'form': form,
    }

    return render(request, template, context)
