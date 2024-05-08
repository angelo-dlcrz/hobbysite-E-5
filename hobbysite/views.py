from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from commissions.models import Commission
from forum.models import Thread
from user_management.models import Profile
from merchstore.models import Transaction
from wiki.models import Article


class HomePageView(TemplateView):
    template_name = 'home.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user.profile
        ctx['user_threads'] = Thread.objects.filter(author=user)
        ctx['my_commissions'] = Commission.objects.filter(
            author=self.request.user.profile)
        ctx['applied_commissions'] = Commission.objects.filter(
            jobs__applications__applicant=self.request.user.profile)
        ctx["transactions"] = Transaction.objects.all()
        ctx["owners"] = Profile.objects.all()
        ctx["buyers"] = Profile.objects.all()
        ctx['my_articles'] = Article.objects.filter(
            author=self.request.user.profile)

        return ctx
