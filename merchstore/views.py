from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ProductType


class MerchListView(ListView):
    model = ProductType
    template_name = 'merch_list.html'


class MerchDetailView(DetailView):
    model = ProductType
    template_name = 'merch_detail.html'