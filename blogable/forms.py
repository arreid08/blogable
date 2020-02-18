from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'blog_content', 'date',)

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('title', 'comment', 'date', 'user',)