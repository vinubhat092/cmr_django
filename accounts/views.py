from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import Orderform
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


def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    orders_count = orders.count()
    print("orders1234",orders)
    context = {"customers":customer,
               "orders":orders,
               "orders_count":orders_count}
    return render(request,"accounts/customer.html",context)

def products(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request,"accounts/products.html",context)

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order , fields=('product','status'))    #inline formsets
    customer = Customer.objects.get(id=pk)
    print("ciah",customer)
    formset = OrderFormSet(instance=customer)                                  
    # form = Orderform(initial={"customer":customer})
    if request.method =="POST":
        form = Orderform(request.POST)
        print("coming12",request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={"formset":formset}
    return render(request,"accounts/create_order.html",context)

def updateOrder(request,pk):
    orderss = Order.objects.get(id=pk)
    form = Orderform(instance=orderss)
    if request.method =="POST":
        form = Orderform(request.POST)
        print("coming",request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={"form":form}
    return render(request,"accounts/create_order.html",context)

def deleteOrder(request,pk):
    orderss = Order.objects.get(id=pk)
    context={"orderss":orderss}
    if request.method == "POST":
        form = Orderform(instance=orderss)
        orderss.delete()
        return redirect("/")
    return render(request,"accounts/delete.html",context)



