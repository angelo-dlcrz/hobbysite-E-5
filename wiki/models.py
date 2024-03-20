from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Article Categories' 


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        'ArticleCategory',
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'categories',
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('wiki:wiki_detail', args = [self.pk])
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_on'] 