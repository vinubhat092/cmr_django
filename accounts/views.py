from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def home(request):
    print("comingnge")
    orders = Order.objects.all()
    customers = Customer.objects.all()
    customers_count = customers.count()
    orders_count = orders.count()
    orders_delivered = orders.filter(status="Delivered").count()
    orders_pending = orders.filter(status="pending").count()
    print("sf",customers)
    context = {
        "orders":orders,
        "customers":customers,
        "orders_count":orders_count,
        "orders_delivered":orders_delivered,
        "orders_pending":orders_pending,
    }
    return render(request,"accounts/dashboard.html",context)

def dashboard(request):
    return render(request,"accounts/dashboard.html")


def customer(request):
    return render(request,"accounts/customer.html")

def products(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request,"accounts/products.html",context)


