from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product


@login_required
def view_bag(request):
    """ a view to return bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """add specific item to the bag"""

    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('', {})

    bag[item_id] = quantity
    messages.success(request, f'Added {product.name} to your bag.')

    request.session['bag'] = bag
    return redirect('view_bag')
