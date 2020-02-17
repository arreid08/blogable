from django.shortcuts import render, redirect
from .models import Post, Comments
from .forms import PostForm, CommentsForm
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blogable/post_list.html', {'posts': posts})

# @login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blogable/post_detail.html', {'post': post})

# @login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_list', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogable/post_form.html', {'form': form})

# @login_required
def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blogable/post_form.html', {'form': form})

# @login_required
def comments_list(request):
    comments = Comments.objects.all()
    return render(request, 'blogable/comments_list.html', {'comments': comments}) 