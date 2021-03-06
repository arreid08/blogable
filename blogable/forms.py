from django import forms
from .models import Blog, Post, Comments

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('name',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'blog_content', 'date',)

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment', 'date', 'user',)