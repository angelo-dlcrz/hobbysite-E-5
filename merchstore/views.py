from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Product, ProductType, Transaction
from .forms import ProductForm, TransactionForm

from user_management.models import Profile


class MerchListView(ListView):
    model = Product
    template_name = 'merch_list.html'

    def get_context_date(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['product_types'] = ProductType.objects.all()
        return ctx


class MerchDetailView(DetailView):
    model = Product
    template_name = 'merch_detail.html'


class MerchCreateView(CreateView):
    model = Product
    template_name = 'merch_create.html'


class MerchUpdateView(UpdateView):
    model = Product
    template_name = 'merch_update.html'


class CartView(ListView):
    model = Transaction
    template_name = 'cart.html'


class TransactionListView(ListView):
    model = Transaction
    template_name = 'transaction_list.html'
