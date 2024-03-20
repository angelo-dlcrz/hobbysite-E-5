from django.contrib import admin

from .models import ProductType, Product


class ProductInLine(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inlines = [ProductInLine,]

    search_fields = ['name',]


admin.site.register(ProductType, ProductTypeAdmin)