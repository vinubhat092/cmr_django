from django.contrib import admin
from django.urls import path ,include
from accounts.views import home,products,customer,dashboard,createOrder,updateOrder,deleteOrder,registerPage,loginPage
urlpatterns = [
    path('', home , name="home"),
    path('register/', registerPage , name="registerPage"),
    path('login/', loginPage , name="loginPage"),
    path('products/', products ,name="products"),
    path('customer/<str:pk_test>/', customer, name="customer" ),
    path('orders/<str:pk>', createOrder, name="createOrder" ),
    path('update/<str:pk>', updateOrder, name="updateOrder" ),
    path('delete/<str:pk>', deleteOrder, name="deleteOrder" ),
    
   
]