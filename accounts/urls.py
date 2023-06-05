from django.contrib import admin
from django.urls import path ,include
from accounts.views import home,products,customer,dashboard
urlpatterns = [
    path('', home ),
    path('products/', products ),
    path('customer/', customer ),
    path('dashboard/', dashboard ),
   
]