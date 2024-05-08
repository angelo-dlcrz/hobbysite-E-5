from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from commissions.models import Commission

from forum.models import Thread
class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user.profile
        context['user_threads'] = Thread.objects.filter(author=user)
        
        return context

    # if self.request.user.is_authenticated:
    #         user = self.request.user.profile
    #         user_threads = Thread.objects.filter(author=user)
    #         for category in categories:
    #             threads_category[category] = Thread.objects.filter(category=category).exclude(author=user)
    #         return {'user_threads': user_threads, 'threads_category': threads_category}
    #     else:
    #         for category in categories:
    #             threads_category[category] = Thread.objects.filter(category=category)
    #         return {'threads_category': threads_category}

    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     # ctx['my_commissions'] = Commission.objects.filter(author=self.request.user.profile)
    #     # ctx['applied_commissions'] = Commission.objects.filter(jobs__applications__applicant=self.request.user.profile)
    #     return ctx