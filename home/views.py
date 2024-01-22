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


def biography(request):
    """ A view to return the biography page """

    return render(request, 'home/biography.html')


def privacy_policy(request):
    """ A view to return the privacy_policy page """

    return render(request, 'home/privacy_policy.html')


def what_is_reiki(request):
    """ A view to return the what_is_reiki page """

    return render(request, 'home/what_is_reiki.html')


def benefits_of_reiki(request):
    """ A view to return the benefits_of_reiki page """

    return render(request, 'home/benefits_of_reiki.html')


def terms_conditions(request):
    """ A view to return the terms_conditions page """

    return render(request, 'home/terms_conditions.html')
