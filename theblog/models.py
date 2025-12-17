from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    x_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default="Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = HTMLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blogpost_likes')
    dislikes = models.ManyToManyField(User, related_name='blog_posts_disliked',)

    def __str__(self):
        return self.title + " by " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.pk),))
