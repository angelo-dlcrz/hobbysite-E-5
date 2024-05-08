from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ArticleCategory(models.Model):
    class Category(models.TextChoices):
        LAPTOPS = 'LAPTOPS'
        PHONES = 'PHONES'
        PROCESSORS = 'PROCESSORS'
        KEYBOARDS = 'KEYBOARDS'
        TELEVISIONS = 'TELEVISIONS'

    name = models.CharField(
        max_length=255, choices=Category.choices, default='TV')
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Article Categories'


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.SET_NULL,
        related_name='article_author',
    )
    category = models.ForeignKey(
        'ArticleCategory',
        null=True,
        on_delete=models.SET_NULL,
        related_name='categories',
    )
    entry = models.TextField()
    header_image = models.ImageField(
        upload_to="images/",
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('wiki:wiki_detail', args=[self.pk])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.SET_NULL,
        related_name='wiki_author',
    )
    article = models.ForeignKey(
        'Article',
        null=True,
        on_delete=models.CASCADE,
        related_name='article',
    )
    entry = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
