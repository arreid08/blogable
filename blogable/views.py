from django.shortcuts import render, redirect
from .models import Blog, Post, Comments
from .forms import BlogForm, PostForm, CommentsForm
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blogable/blog_list.html', {'blogs': blogs})

# @login_required
def blog_detail(request, pk):
    blogs = Blog.objects.all()
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blogable/blog_detail.html', {'blogs': blogs, 'blog': blog})

# @login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('/')
    else:
        form = BlogForm()
    return render(request, 'blogable/blog_form.html', {'form': form})

# @login_required
def post_list(request):
    # blogs = Blog.objects.get(pk=pk)
    posts = Post.objects.all()
    return render(request, 'blogable/post_list.html', {'posts': posts})
    #, 'blogs': blogs

# @login_required
def post_detail(request, pk):
    blogs = Blog.objects.all()
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentsForm()
    return render(request, 'blogable/post_detail.html', {'blogs': blogs, 'post': post, 'form': form})

# @login_required
def post_create(request, pk):
    blogs = Blog.objects.all()
    post = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog_id = pk
            post.save()
            return redirect('blog_detail', pk=pk)
    else:
        form = PostForm()
    return render(request, 'blogable/post_form.html', {'form': form})

# @login_required
def post_update(request, pk):
    blogs = Blog.objects.all()
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            # post.blog_id = pk
            # post.save()
            return redirect('blog_detail', pk=post.blog_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogable/post_form.html', {'blogs': blogs, 'form': form})

# @login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    blog = post.blog_id
    Post.objects.get(pk=pk).delete()
    return redirect('blog_detail', pk=blog)

# @login_required
def comments_list(request):
    blogs = Blog.objects.all()
    comments = Comments.objects.all()
    return render(request, 'blogable/comments_list.html', {'blogs': blogs, 'comments': comments}) 

# @login_required
def comments_delete(request, pk):
    comments = Comments.objects.get(pk=pk)
    post = comments.post_id
    Comments.objects.get(pk=pk).delete()
    return redirect('list_detail', pk=post)