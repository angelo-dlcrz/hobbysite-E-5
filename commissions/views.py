from django.http import HttpRequest, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.db import transaction

from .models import Commission, Job, JobApplication
from user_management.models import Profile
from .forms import CommissionForm, JobForm, JobApplicationForm, jobformset


class CommissionListView(ListView):
    model = Commission
    template_name = 'commission_list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and Profile.objects.filter(user=self.request.user).exists():
            ctx['my_commissions'] = Commission.objects.filter(author=self.request.user.profile)
            ctx['applied_commissions'] = Commission.objects.filter(jobs__applications__applicant=self.request.user.profile)
        return ctx


class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = 'commission_detail.html'

    def post(self, request, *args, **kwargs):
        job_role = request.POST.get('job_role')

        jobs = Job.objects.get(
            role=job_role, commission=self.get_object())
        job_application = JobApplication(
            job=jobs,
            applicant=request.user.profile,
            application_status='PENDING'
        )
        job_application.save()
        total_applications = jobs.applications.count()
        remaining_manpower = jobs.manpower - total_applications

        if remaining_manpower == 0:
            jobs.job_status = 'FULL'
            jobs.save()

        commission = self.get_object() 
        if commission.jobs.filter(job_status='FULL').count() == commission.jobs.count():
            commission.commission_status = 'FULL'
            commission.save()
        return redirect('commissions:commission_detail', pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        commission = self.object
        if Profile.objects.filter(user=self.request.user).exists():
            context['applied_jobs'] = commission.jobs.filter(
                applications__applicant=self.request.user.profile)
        jobs_data = []
        for job in commission.jobs.all():
            total_applications = job.applications.count()
            remaining_manpower = job.manpower - total_applications
            jobs_data.append({
                'job': job,
                'total_applications': total_applications,
                'remaining_manpower': remaining_manpower,
            })
        context['jobs_data'] = jobs_data
        return context


class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commission_create.html'
    fields = ['title', 'description', 'commission_status']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['jobs'] = jobformset(self.request.POST)
        else:
            context['jobs'] = jobformset()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        context = self.get_context_data()
        jobs = context['jobs']
        with transaction.atomic():
            self.object = form.save()

            if jobs.is_valid():
                jobs.instance = self.object
                jobs.save()
        return super().form_valid(form)


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = 'job_create.html'
    form_class = JobForm

    def get_success_url(self):
        return reverse_lazy('commissions:commission_detail', kwargs={'pk': self.object.commission.pk})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['commission_pk'] = self.kwargs['pk']
        return ctx

    def form_valid(self, form):
        form.instance.commission = Commission.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    template_name = 'update.html'
    form_class = CommissionForm

class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'update.html'
    def get_success_url(self):
        return reverse_lazy('commissions:commission_detail', kwargs={'pk': self.object.commission.pk})
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def post(self, request: HttpRequest, *args: str, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        job = self.get_object()
        commission = job.commission

        if commission.jobs.filter(job_status='OPEN').exists():
            commission.commission_status = 'OPEN'
            commission.save()
        elif commission.jobs.filter(job_status='FULL').count() == commission.jobs.count():
            commission.commission_status = 'FULL'
            commission.save()

        return response

class JobApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'update.html'

    def get_success_url(self):
        return reverse_lazy('commissions:commission_detail', kwargs={'pk': self.object.job.commission.pk})