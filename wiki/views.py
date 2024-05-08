from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article, ArticleCategory, Profile
from .forms import ArticleCreateForm, ArticleUpdateForm

import random


class WikiListView(ListView):
    model = Article
    template_name = 'wiki_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        
        laptop_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='LAPTOPS'))
        phone_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='PHONES'))
        processor_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='PROCESSORS'))
        keyboard_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='KEYBOARDS'))
        tv_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='TELEVISIONS'))

        if current_user.is_authenticated:
            context['user_articles'] = Article.objects.filter(author=Profile.objects.get(user=current_user))
            context['laptop_articles'] = laptop_articles.exclude(author=Profile.objects.get(user=current_user))
            context['phone_articles'] = phone_articles.exclude(author=Profile.objects.get(user=current_user))
            context['processor_articles'] = processor_articles.exclude(author=Profile.objects.get(user=current_user))
            context['keyboard_articles'] = keyboard_articles.exclude(author=Profile.objects.get(user=current_user))
            context['tv_articles'] = tv_articles.exclude(author=Profile.objects.get(user=current_user))
        else:
            context['laptop_articles'] = laptop_articles
            context['phone_articles'] = phone_articles
            context['processor_articles'] = processor_articles
            context['keyboard_articles'] = keyboard_articles
            context['tv_articles'] = tv_articles

        return context
class WikiDetailView(DetailView):
    model = Article
    template_name = 'wiki.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_article = Article.objects.get(pk=self.kwargs['pk'])
        current_category = current_article.category
        other_articles = Article.objects.exclude(pk=self.kwargs['pk']).filter(category=current_category)
        read_others = random.sample(list(other_articles), 2)
        article_image = current_article.header_image
        
        context['current_article'] = current_article
        context['current_category'] = current_category
        context['other_articles'] = other_articles
        context['read_others'] = read_others
        context['article_image'] = article_image

        return context
    

class WikiCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'wiki_create.html'

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class WikiUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'wiki_create.html'