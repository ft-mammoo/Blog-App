from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    likes = models.ManyToManyField(User, related_name='blogpost_likes')

    def __str__(self):
        return self.title + " by " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.pk),))