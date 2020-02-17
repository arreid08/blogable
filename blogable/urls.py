from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('comments_list/', views.comments_list, name='comments_list')
]