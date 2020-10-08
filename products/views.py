from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Product

@login_required
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
