from django import forms
from django.contrib import admin

from .models import Product, Transaction


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_type': forms.Select(),
            'status': forms.Select(),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('amount', )
