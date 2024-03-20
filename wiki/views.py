from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse

from .models import Article


class WikiListView(ListView):
    model = Article
    template_name = 'wiki_list.html'
    context_object_name = 'articles'


class WikiDetailView(DetailView):
    model = Article
    template_name = 'wiki.html'