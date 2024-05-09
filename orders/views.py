from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Order, Customer, Product
from .forms import OrderForm

from django.urls import reverse


def home(request):
    orders = Order.objects.all()
    return render(request, 'orders/home.html', {'orders': orders})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def total_sales_by_product_and_customer(request, product_id, customer_id):
    orders = Order.objects.filter(product_id=product_id, customer_id=customer_id)
    total_sales = sum(order.total_price for order in orders)
    return render(request, 'orders/total_sales.html', {'total_sales': total_sales})

def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_add.html', {'form': form})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect(reverse('order_list'))

def orders_by_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = Order.objects.filter(customer=customer)
    return render(request, 'orders/orders_by_customer.html', {'orders': orders})

def orders_by_product(request, product_id):
    product = Product.objects.get(id=product_id)
    orders = Order.objects.filter(product=product)
    return render(request, 'orders/orders_by_product.html', {'orders': orders})

def total_sales_by_product(request, product_id):
    product = Product.objects.get(id=product_id)
    orders = Order.objects.filter(product=product)
    total_sales = sum(order.total_price for order in orders)
    return render(request, 'orders/total_sales_by_product.html', {'total_sales': total_sales})
def total_sales_by_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    orders = Order.objects.filter(customer=customer)
    total_sales = sum(order.total_price for order in orders)
    return render(request, 'orders/total_sales_by_customer.html', {'total_sales': total_sales})
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'orders/customer_list.html', {'customers': customers})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'orders/product_list.html', {'products': products})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})