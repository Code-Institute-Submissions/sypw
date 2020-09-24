from django.shortcuts import render, redirect
from django.urls import reverse


def view_bag(request):
    """ a view to return bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    quantity = 1
    redirect_url = 'view_bag'
    bag = request.session.get('bag', {})
    bag[item_id] = quantity

    request.session['bag'] = bag
    # print(request.session['bag'])

    return redirect(redirect_url)
