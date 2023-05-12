from django.urls import path
from .views import shop_index, products_list, order_list

app_name = 'shopapp'
urlpatterns = [
    path('', shop_index, name='shop_index'),
    path('products/', products_list, name='products_list'),
    path('orders/', order_list, name='order_list'),
]
