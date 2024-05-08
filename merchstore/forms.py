from django import forms
from django.contrib import admin

from .models import Product, Transaction


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_type',
                  'description', 'price', 'stock', 'status']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('amount', )
