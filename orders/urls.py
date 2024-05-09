from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_add/', views.order_add, name='order_add'),
    path('order_delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('orders/customer/<int:customer_id>/', views.orders_by_customer, name='orders_by_customer'),
    path('orders/product/<int:product_id>/', views.orders_by_product, name='orders_by_product'),
    path('sales/product/<int:product_id>/', views.total_sales_by_product, name='total_sales_by_product'),
    path('sales/customer/<int:customer_id>/', views.total_sales_by_customer, name='total_sales_by_customer'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('product_list/', views.product_list, name='product_list'),  # new URL pattern
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    # path('sales/product/<int:product_id>/customer/<int:customer_id>/', views.total_sales_by_product_and_customer, name='total_sales_by_product_and_customer'),
    path('sales/product/<int:product_id>/', views.total_sales_by_product, name='total_sales_by_product'),
    path('sales/customer/<int:customer_id>/', views.total_sales_by_customer, name='total_sales_by_customer'),
]