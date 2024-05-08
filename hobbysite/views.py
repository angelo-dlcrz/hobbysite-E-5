from django.shortcuts import render
from django.views.generic import TemplateView

from commissions.models import Commission
from user_management.models import Profile
from merchstore.models import Transaction


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['my_commissions'] = Commission.objects.filter(
            author=self.request.user.profile)
        ctx['applied_commissions'] = Commission.objects.filter(
            jobs__applications__applicant=self.request.user.profile)
        ctx["transactions"] = Transaction.objects.all()
        ctx["owners"] = Profile.objects.all()
        ctx["buyers"] = Profile.objects.all()

        return ctx
