from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Thread Categories"


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='thread_author')
    category = models.ForeignKey(ThreadCategory, on_delete=models.SET_NULL, null=True, related_name='category')
    entry = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum:thread', args=[self.pk])
    
    class Meta:
        ordering = ['-created_on']


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='comment_author')
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='thread')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entry
    
    class Meta:
        ordering = ['created_on']