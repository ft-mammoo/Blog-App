from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm, EditBlogPostForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = BlogPost
    template_name = 'home.html'
    ordering = ['-created_at']

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

class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    