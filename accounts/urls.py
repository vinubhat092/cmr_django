from django.contrib import admin
from django.urls import path ,include
from django.contrib.auth import views as auth_views
from accounts.views import home,products,customer,dashboard,createOrder,updateOrder,deleteOrder,registerPage,loginPage,logoutPage,userPage,accountSettings
urlpatterns = [
    path('', home , name="home"),
    path('register/', registerPage , name="registerPage"),
    path('login/', loginPage , name="loginPage"),
    path('user/', userPage , name="userPage"),
    path('account/', accountSettings , name="account"),
    path('logout/', logoutPage , name="logoutPage"),
    path('products/', products ,name="products"),
    path('customer/<str:pk_test>/', customer, name="customer" ),
    path('orders/<str:pk>', createOrder, name="createOrder" ),
    path('update/<str:pk>', updateOrder, name="updateOrder" ),
    path('delete/<str:pk>', deleteOrder, name="deleteOrder" ),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name = "reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name = "password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
    
   
]