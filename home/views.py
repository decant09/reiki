from django.shortcuts import render
from review.models import Review

# Create your views here.

def index(request):
    """ A view to return the index page """

    reviews = Review.objects.filter(homepage=True)
    context = {
        'homepage_reviews': reviews,
    }

    return render(request, 'home/index.html', context)
