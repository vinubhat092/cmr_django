from django.contrib import admin
from django.urls import path ,include
from accounts.views import home,products,customer,dashboard,createOrder,updateOrder,deleteOrder
urlpatterns = [
    path('', home , name="home"),
    path('products/', products ,name="products"),
    path('customer/<str:pk_test>/', customer, name="customer" ),
    path('orders/', createOrder, name="createOrder" ),
    path('update/<str:pk>', updateOrder, name="updateOrder" ),
    path('delete/<str:pk>', deleteOrder, name="deleteOrder" ),
    
   
]