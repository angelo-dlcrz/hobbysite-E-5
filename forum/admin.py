from django.contrib import admin
from .models import Post, PostCategory


class PostInline(admin.TabularInline):
    model = Post

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory

    inlines = [PostInline,]


class PostAdmin(admin.ModelAdmin):
    model = Post

admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
