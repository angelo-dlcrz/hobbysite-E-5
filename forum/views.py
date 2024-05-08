from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Thread, ThreadCategory, Comment

from .forms import ThreadForm, ThreadUpdateForm, CommentForm


class ThreadListView(ListView):
    model = Thread
    template_name = 'forum_list.html'
    context_object_name = 'threads_context'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = ThreadCategory.objects.all()
        threads_category_dict = {}

        if self.request.user.is_authenticated:
            user = self.request.user.profile
            for category in categories:
                threads_category_dict[category] = Thread.objects.filter(category=category).exclude(author=user)
            context['user_threads'] = Thread.objects.filter(author=user)
            context['threads_category'] = threads_category_dict
        else:
            for category in categories:
                threads_category_dict[category] = Thread.objects.filter(category=category)
            context['threads_category'] = threads_category_dict
        
        return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum_detail.html'
    context_object_name = 'thread'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['more_threads'] = Thread.objects.filter(category=self.object.category).exclude(pk=self.object.pk)[:2]
        context['comments'] = Comment.objects.filter(thread=self.object)
        context['comments_form'] = CommentForm()

        if self.request.user == self.object.author.user:
            context['is_owner'] = True
        else:
            context['is_owner'] = False

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.author = request.user.profile
                comment.thread = self.object
                comment.save()
        return self.get(request, *args, **kwargs)
    

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = '__all__'
    template_name = 'forum_create.html'
    context_object_name = 'thread'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ThreadForm()

        return context

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                thread = form.save(commit=False)
                thread.author = request.user.profile
                thread.save()
                print(thread.pk)
                return redirect('forum:thread', pk=thread.pk)
        return self.get(request, *args, **kwargs)
    

class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    fields = '__all__'
    template_name = 'forum_update.html'
    context_object_name = 'thread'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ThreadUpdateForm()

        if self.request.user == self.object.author.user:
            context['is_owner'] = True
        else:
            context['is_owner'] = False

        return context

    def post(self, request, *args, **kwargs):
        form = ThreadUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                thread = form.save(commit=False)                
                thread_old = Thread.objects.get(pk=self.get_object().pk)
                thread_old.title = thread.title
                thread_old.category = thread.category
                thread_old.entry = thread.entry
                thread_old.image = thread.image
                thread_old.save()
                return redirect('forum:thread', pk=thread_old.pk)
        return self.get(request, *args, **kwargs)