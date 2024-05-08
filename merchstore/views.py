from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login

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
    form_class = TransactionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                product = self.get_object()
                transaction = form.save(commit=False)
                transaction.product = product
                transaction.buyer = request.user.profile
                transaction.amount = form.cleaned_data["quantity"]

                if product.stock >= transaction.amount > 0:
                    transaction.save()

                    product.stock -= transaction.amount
                    if product.stock == 0:
                        product.status = "Out of Stock"
                    product.save()

                    return redirect("merchstore:cart")
            else:
                return redirect_to_login(next=request.get_full_path())
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)


class MerchCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'merch_create.html'
    form_class = ProductForm

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class MerchUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'merch_update.html'
    fields = ['name', 'product_type', 'description', 'price', 'stock']
    success_url = reverse_lazy('merchstore:merch_list')\


    def form_valid(self, form):
        product = form.save(commit=False)
        if product.stock == 0:
            product.status = "Out of Stock"
        else:
            product.status = "Available"
        product.save()
        return super().form_valid(form)


class CartView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["owners"] = Profile.objects.all()
        return ctx


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["buyers"] = Profile.objects.all()
        return ctx
