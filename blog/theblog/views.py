from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost
from .forms import BlogPostForm

class HomePageView(ListView):
    model = BlogPost
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = BlogPost
    template_name = 'article_details.html'

class CreatePostView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create_post.html'