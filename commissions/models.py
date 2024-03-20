from django.db import models
from django.urls import reverse


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission_detail', args=[self.pk])
    
    def get_first_words(self):
        return self.description[:500]
    
    def exceeds(self):
        return len(self.description)>500
    
    class Meta:
        ordering = ['created_on']


class Comment(models.Model):
    commission = models.ForeignKey(
        'Commission',
        on_delete = models.CASCADE,
        related_name = 'comments'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.commission.title, str(self.created_on))
    
    class Meta:
        ordering = ['-created_on']
