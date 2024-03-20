from django.urls import path

from .views import WikiListView, WikiDetailView


urlpatterns = [
    path('articles/', WikiListView.as_view(), name = 'wiki_list'),
    path('article/<int:pk>', WikiDetailView.as_view(), name = 'wiki_detail'),
]

app_name = 'wiki'