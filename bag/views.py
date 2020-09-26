from django.shortcuts import render, redirect


def view_bag(request):
    """ a view to return bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """add specific item to the bag"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('', {})

    bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect('view_bag')
