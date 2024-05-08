from django.contrib import admin
from .models import Thread, ThreadCategory, Comment


class ThreadInline(admin.TabularInline):
    model = Thread


class CommentInLine(admin.TabularInline):
    model = Comment

class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory

    inlines = [ThreadInline,]


class ThreadAdmin(admin.ModelAdmin):
    model = Thread

    inlines = [CommentInLine,]


class CommentAdmin(admin.ModelAdmin):
    model = Comment

admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)