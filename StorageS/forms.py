from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Product, Client


class LoginForm(AuthenticationForm):
    pass


class AddProduct(forms.ModelForm):
    product_count = forms.IntegerField()

    class Meta:
        model = Product
        fields = ['product_name',
                  'product_category',
                  'product_made',
                  'product_cost', ]


class BasketClient(forms.ModelForm):
    address = forms.CharField(max_length=50)

    class Meta:
        model = Client
        fields = ['client_name',
                  'client_passport',
                  'client_birthday']
