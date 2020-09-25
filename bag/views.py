from django.shortcuts import render, redirect


def view_bag(request):
    """ a view to return bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    bag = {}
    quantity = int(request.POST.get('quantity', 1))
    bag = request.session.get('bag')

    bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])

    return redirect('view_bag')
