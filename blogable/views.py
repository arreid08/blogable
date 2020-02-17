from django.shortcuts import render
from .models import Post, Comments

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blogable/post_list.html', {'posts': posts})

def comments_list(request):
    comments = Comments.objects.all()
    return render(request, 'blogable/comments_list.html', {'comments': comments}) 