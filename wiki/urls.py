from django.urls import path

from .views import WikiListView, WikiDetailView, WikiCreateView, WikiUpdateView


urlpatterns = [
    path('articles/', WikiListView.as_view(), name ='wiki_list'),
    path('article/<int:pk>', WikiDetailView.as_view(), name ='wiki_detail'),
    path('article/add/', WikiCreateView.as_view(), name ='wiki_create'),
    path('article/<int:pk>/edit/', WikiUpdateView.as_view(), name ='wiki_update'),
]

app_name = 'wiki'