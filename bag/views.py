from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ a view to return bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """add specific item to the bag"""

    product = Product.objects.get(pk=item_id)

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('', {})

    bag[item_id] = quantity
    messages.success(request, f'Added {product.name} to your bag.')

    request.session['bag'] = bag
    return redirect('view_bag')
