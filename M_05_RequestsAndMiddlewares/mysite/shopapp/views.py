from timeit import default_timer

from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Product, Order


def shop_index(request: HttpRequest):
    # return HttpResponse('<h1>Hello epta</h1>')
    context = {
        'time_running': default_timer(),
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shopapp/products-list.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all()
    }
    return render(request, 'shopapp/orders-list.html', context=context)
