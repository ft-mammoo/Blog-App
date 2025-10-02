from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title + " by " + str(self.author)