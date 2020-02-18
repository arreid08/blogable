from django.db import models

# Create your models here.
#  
class Blog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='post', default='')
    title = models.CharField(max_length=100)
    published = 'published'
    draft = 'draft'
    status = [(published, 'published'), (draft, 'draft')]
    blog_content = models.TextField(default='Your blog post here')
    date = models.DateField()

    def __str__(self):
        return self.title

class Comments(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    comment = models.CharField(max_length=500)
    date = models.DateField()
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.comment