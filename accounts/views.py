from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def home(request):
    return render(request,"accounts/main.html")

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


