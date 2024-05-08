from django.urls import path

from .views import ThreadListView, ThreadDetailView, ThreadCreateView, ThreadUpdateView

urlpatterns = [
    path('threads', ThreadListView.as_view(), name='threads'),
    path('thread/<int:pk>', ThreadDetailView.as_view(), name='thread'),
    path('thread/add', ThreadCreateView.as_view(), name='add_thread'),
    path('thread/<int:pk>/edit', ThreadUpdateView.as_view(), name='edit_thread')
]

app_name = 'forum'