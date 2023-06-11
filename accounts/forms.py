from django.forms import ModelForm

from .models import Order



class Orderform(ModelForm):   #MODEL FORM
    class Meta:
        model = Order
        # fields = ['customer','product'] one more way of choosing fields manually
        fields = '__all__'
