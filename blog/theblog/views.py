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

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['cat_list'] = cat_list
        return context

def CategoryView(request, categs):
    category_posts = BlogPost.objects.filter(category__name__iexact=categs.replace('-', ' '))
    return render(request, 'categories.html', {'categs': categs.title().replace(' ', '-'), 'category_posts': category_posts})

class ArticleDetailView(DetailView):
    model = BlogPost
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['cat_list'] = cat_list
        return context

class CreatePostView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(CreatePostView, self).get_context_data(*args, **kwargs)
        context['cat_list'] = cat_list
        return context

class CreateCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'create_category.html'

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(CreateCategoryView, self).get_context_data(*args, **kwargs)
        context['cat_list'] = cat_list
        return context

class EditPostView(UpdateView):
    model = BlogPost
    form_class = EditBlogPostForm
    template_name = 'edit_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(EditPostView, self).get_context_data(*args, **kwargs)
        context['cat_list'] = cat_list
        return context

class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_list = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context['cat_list'] = cat_list
        return context
