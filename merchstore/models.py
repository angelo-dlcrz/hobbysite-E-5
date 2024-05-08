from django.db import models
from django.urls import reverse

from user_management.models import Profile


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"

    def __str__(self):
        return self.name


class Product(models.Model):
    product_status = (
        ("Available", "Available"),
        ("On Sale", "On Sale"),
        ("Out of Stock", "Out of Stock"),
    )

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=18, decimal_places=2)
    stock = models.PositiveIntegerField(null=True)
    status = models.CharField(
        max_length=32,
        choices=product_status,
        default="Available",
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merchstore:merch_detail", kwargs={"pk": self.pk})


class Transaction(models.Model):
    transaction_status = (
        ("On Cart", "On Cart"),
        ("To Pay", "To Pay"),
        ("To Ship", "To Ship"),
        ("To Receive", "To Receive"),
        ("Delivered", "Delivered"),
    )

    buyer = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )
    amount = models.PositiveIntegerField()
    status = models.CharField(
        max_length=32,
        choices=transaction_status,
        null=True,
        default="On Cart",
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.product} - {self.status}"
