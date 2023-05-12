from timeit import default_timer

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Product, Orders


def shop_index(request: HttpRequest):
    context = {
        'time_running': default_timer(),
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def products_list(request: HttpRequest):
    context = {
        'products': Product.objects.all()
    }

    return render(request, 'shopapp/product-list.html', context=context)


def order_list(request: HttpRequest):
    context = {
        'orders': Orders.objects.select_related('user').prefetch_related('products').all()
    }

    return render(request, 'shopapp/order-list.html', context=context)
