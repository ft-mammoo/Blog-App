from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BlogPost
from .forms import BlogPostForm, EditBlogPostForm

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

class EditPostView(UpdateView):
    model = BlogPost
    form_class = EditBlogPostForm
    template_name = 'edit_post.html'
    