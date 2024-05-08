from django.shortcuts import render
from django.views.generic import TemplateView

from user_management.models import Profile
from merchstore.models import Transaction


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["transactions"] = Transaction.objects.all()
        ctx["owners"] = Profile.objects.all()
        ctx["buyers"] = Profile.objects.all()
        return ctx
