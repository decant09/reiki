from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Review
from .forms import ReviewForm


def review(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
    else:
        user = None

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save()
            review.user = user
            review.save()

            messages.success(request, "Review successfully posted. " +
                             "Your review will be displayed once approved. " +
                             "Thank You.")
            return redirect(reverse('review'))
        else:
            messages.error(request, "You didn't complete the required " +
                           "fields, please complete the form again.")

    else:
        form = ReviewForm()

    context = {
        'reviews': Review.objects.filter(is_approved=True),
        'form': form,
    }

    return render(request, 'review/review.html', context)
