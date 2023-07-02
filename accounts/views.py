from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import Orderform,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.
from .models import *

@login_required(login_url="loginPage")
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

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        print("cdsd")
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for" + user)
            return redirect('loginPage')
    context={"form":form}
    return render(request,"accounts/register.html",context)

@unauthenticated_user
def loginPage(request):
    
    if request.method == "POST":
        print("csd")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("dsdj")
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"username or password is incorrect")


    context={}
    return render(request,"accounts/login.html",context)

def logoutPage(request):
    logout(request)
    return redirect("loginPage")
@login_required(login_url="loginPage")
def dashboard(request):
    return render(request,"accounts/dashboard.html")

@login_required(login_url="loginPage")
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    orders_count = orders.count()
    # print("orders1234",orders)
    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs
    context = {"customers":customer,
               "orders":orders,
               "orders_count":orders_count,
               "my_filter":my_filter}
    return render(request,"accounts/customer.html",context)
@login_required(login_url="loginPage")
def products(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request,"accounts/products.html",context)
@login_required(login_url="loginPage")
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order , fields=('product','status') ,extra=10)    #inline formsets
    customer = Customer.objects.get(id=pk)
    print("ciah",customer)
    formset = OrderFormSet()                                  
    # form = Orderform(initial={"customer":customer})
    if request.method =="POST":
        # form = Orderform(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)  
        print("coming12",request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={"formset":formset}
    return render(request,"accounts/create_order.html",context)
@login_required(login_url="loginPage")
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
@login_required(login_url="loginPage")
def deleteOrder(request,pk):
    orderss = Order.objects.get(id=pk)
    context={"orderss":orderss}
    if request.method == "POST":
        form = Orderform(instance=orderss)
        orderss.delete()
        return redirect("/")
    return render(request,"accounts/delete.html",context)



