from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Product Types"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("merchstore:merch_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        'ProductType',
        on_delete=models.SET_NULL,
        null = True,
        related_name = "products"
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
