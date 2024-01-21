from django.shortcuts import render
from .models import Review


def review(request):

    context = {
        'reviews': Review.objects.all(),
    }

    return render(request, 'review/review.html', context)
