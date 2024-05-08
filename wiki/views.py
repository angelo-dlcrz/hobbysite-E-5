from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article, ArticleCategory, Profile


class WikiListView(ListView):
    model = Article
    template_name = 'wiki_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        
        laptop_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='LP'))
        phone_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='PH'))
        processor_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='PR'))
        keyboard_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='KB'))
        tv_articles = Article.objects.filter(category=ArticleCategory.objects.get(name='TV'))

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