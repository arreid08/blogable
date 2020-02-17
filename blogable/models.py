from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    published = 'published'
    draft = 'draft'
    status = [(published, 'published'), (draft, 'draft')]
    blog = models.TextField(default='Your blog post here')
    date = models.DateField()

    def __str__(self):
        return self.title

class Comments(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='content')
    content = models.CharField(max_length=500)
    date = models.DateField()
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.content