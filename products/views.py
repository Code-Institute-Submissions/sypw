from django.shortcuts import render

from .models import Product


def products(request):
    """ a view to return products page """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def decide(request):
    """ a view to return products page """

    return render(request, 'products/decide.html')
