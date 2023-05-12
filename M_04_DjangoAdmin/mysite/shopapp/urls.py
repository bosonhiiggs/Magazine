from .views import shop_index, groups_list, orders_list, products_list
from django.urls import path


app_name = 'shopapp'
urlpatterns = [
    path('', shop_index, name='shop_index'),
    path('groups/', groups_list, name='groups_list'),
    path('orders/', orders_list, name='orders_list'),
    path('products/', products_list, name='products_list'),
]