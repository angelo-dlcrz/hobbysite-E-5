from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product


class MerchListView(ListView):
    model = Product
    template_name = 'merch_list.html'


class MerchDetailView(DetailView):
    model = Product
    template_name = 'merch_detail.html'
