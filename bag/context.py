# from decimal import Decimal
from django.conf import settings
from . import product


def bag_contents(request):

    bag_items = []
    total = 0

    total = product.price

    context = {
        'bag_items': bag_items,
        'total': total,
        }

    return context
