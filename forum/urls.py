from django.urls import path

from .views import ForumListView, ForumDetailView

urlpatterns = [
    path('threads', ForumListView.as_view(), name='threads'),
    path('thread/<int:pk>', ForumDetailView.as_view(), name='thread')
]

app_name = 'forum'