from django.shortcuts import render


from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.filter(is_active=True)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
