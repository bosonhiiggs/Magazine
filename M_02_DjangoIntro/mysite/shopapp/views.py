from timeit import default_timer

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 1999),
        ('Desktop', 2999),
        ('Phone', 999),
    ]
    office = [
        ('Laptop repair display ', 249),
        ('Desktop repair monitor ', 199),
        ('Phone repair display ', 399),
    ]
    context = {
        'time_running': default_timer(),
        'products': products,
        'office': office,
    }
    return render(request, 'shopapp/shop-index.html', context=context)
