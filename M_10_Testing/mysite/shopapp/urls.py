from django.urls import path

from .views import (
    shop_index,
    groups_list,

    ProductsListView,
    ProductDetailsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,

    OrdersListView,
    OrderDetailsView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    ProductsExportView,
    OrdersExportView,
    )

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", groups_list, name="groups_list"),

    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/export/", ProductsExportView.as_view(), name="products-export"),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),


    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/export/", OrdersExportView.as_view(), name="orders-export"),
    path("orders/<int:pk>/", OrderDetailsView.as_view(), name="order_details"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order_delete"),
    path("orders/create/", OrderCreateView.as_view(), name="order_create"),
]
