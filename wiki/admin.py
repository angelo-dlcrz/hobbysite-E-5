from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Article, ArticleCategory


class ArticleInline(admin.TabularInline):
    model = Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [
        ArticleInline,
    ]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
