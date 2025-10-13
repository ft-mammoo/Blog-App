from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Category
from .forms import BlogPostForm, EditBlogPostForm
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = BlogPost
    template_name = 'home.html'
    categs = Category.objects.all()
    ordering = ['-created_at']


def CategoryView(request, categs):
    category_posts = BlogPost.objects.filter(category__name__iexact=categs.replace('-', ' '))
    return render(request, 'categories.html', {'categs': categs.title().replace(' ', '-'), 'category_posts': category_posts})

class ArticleDetailView(DetailView):
    model = BlogPost
    template_name = 'article_details.html'

class CreatePostView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create_post.html'

class CreateCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'create_category.html'

class EditPostView(UpdateView):
    model = BlogPost
    form_class = EditBlogPostForm
    template_name = 'edit_post.html'

class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
