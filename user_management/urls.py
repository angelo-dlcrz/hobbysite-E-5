from django.contrib import admin
from django.urls import path

from .views import UserLoginView, UserLogoutView, UserCreateView


urlpatterns = [
    path('login_user/', UserLoginView.as_view(), name='login-user'),
    path('logout_user/', UserLogoutView.as_view(), name='logout-user'),
    path('register_user/', UserCreateView.as_view(), name='register-user'),
]

app_name = 'user_management'