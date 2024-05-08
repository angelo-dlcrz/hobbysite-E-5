"""
URL configuration for hobbysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import HomePageView, DashboardView
from user_management.views import ProfileUpdateView


urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls', namespace='forum')),
    path('merchstore/', include('merchstore.urls', namespace='merchstore')),
    path('wiki/', include('wiki.urls', namespace='wiki')),
    path('commissions/', include('commissions.urls', namespace='commissions')),
    path('profile', ProfileUpdateView.as_view(), name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('user_management.urls', namespace='user_management')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)