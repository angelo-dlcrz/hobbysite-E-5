from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import UserLoginForm, UserRegisterForm, ProfileUpdateForm
from .models import Profile


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class()
        message = ''

        return render(request, self.template_name, {'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = f'Login failed.'

        return render(request, self.template_name, {'form': form, 'message': message})
    

class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('home')
    

class UserCreateView(View):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request, self.template_name, {'form': form})
        

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        context['form'] = ProfileUpdateForm(instance=profile)

        return context
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        profile_form = ProfileUpdateForm(request.POST)

        if 'save' in request.POST:
            if profile_form.is_valid():
                profile.display_name = profile_form.cleaned_data['display_name']
                profile.email_address = profile_form.cleaned_data['email_address']
                profile.save()
                user.username = profile_form.cleaned_data['display_name']
                user.email = profile_form.cleaned_data['email_address']
                user.save()
                return redirect('home')
            
        return render(request, self.template_name)
                
        
        


    
    