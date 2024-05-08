from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = TransactionForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        product = self.get_object()

        if form.is_valid():
            if request.user.is_authenticated():
                transaction = form.save(commit=False)
                transaction.buyer = request.user.profile
                transaction.product = product
                transaction.status = "On Cart"
                transaction.save()

                product.stock -= transaction.amount
                product.save()
                return redirect('merchstore:cart')
            else:
                return redirect('login-user')
        return self.render_to_response(self.get_context_data(form=form))


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
