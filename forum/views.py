from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


class ForumListView(ListView):
    model = Post
    template_name = 'forum_list.html'


class ForumDetailView(DetailView):
    model = Post
    template_name = 'forum_detail.html'