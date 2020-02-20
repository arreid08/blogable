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
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blogable/blog_detail.html', {'blog': blog})

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
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            # item is created in the code but not saved in the database yet.
            comment = form.save(commit=False)
            # this associates the comment with a post.
            comment.post_id = pk
            # this save commits it to the database.
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentsForm()
    return render(request, 'blogable/post_detail.html', {'post': post, 'form': form})

# @login_required
def post_create(request, pk):
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
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    blog = post.blog_id
    Post.objects.get(pk=pk).delete()
    return redirect('blog_detail', pk=blog)

# @login_required
def comments_list(request):
    comments = Comments.objects.all()
    return render(request, 'blogable/comments_list.html', {'comments': comments}) 

# @login_required
def comments_delete(request, pk):
    comments = Comments.objects.get(pk=pk)
    post = comments.post_id
    Comments.objects.get(pk=pk).delete()
    return redirect('list_detail', pk=post)