from django import forms

from .models import Article, Comment

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']


class CommentForm(forms.ModelForm):
    entry = forms.CharField(widget=forms.Textarea, label="Comment")
    class Meta:
        model = Comment
        fields = ['entry']