from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.blog_list, name='blog_list'),
    # path('blog_list', views.blog_list, name='blog_list'),
    path('blog/new', views.blog_create, name='blog_create'),
    path('blog/<int:pk>', views.blog_detail, name='blog_detail'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/new', views.post_create, name='post_create'),
    path('post/<int:pk>/update', views.post_update, name='post_update'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('comments_list/', views.comments_list, name='comments_list'),
]