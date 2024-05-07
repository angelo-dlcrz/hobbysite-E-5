from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import Profile, User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=63)
    email = forms.EmailField()
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Confirm Password')
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'email_address']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']