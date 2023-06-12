from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order



class Orderform(ModelForm):   #MODEL FORM
    class Meta:
        model = Order
        # fields = ['customer','product'] one more way of choosing fields manually
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']