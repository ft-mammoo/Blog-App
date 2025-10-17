from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost, Category
from .forms import BlogPostForm, EditBlogPostForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    postblog = get_object_or_404(BlogPost, id=pk)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('article-detail', args=[str(pk)]))
    if request.method == 'POST':        
        if postblog.likes.filter(id=request.user.id).exists():
            postblog.likes.remove(request.user)
        else:
            postblog.likes.add(request.user)
        return HttpResponseRedirect(reverse_lazy('article-detail', args=[str(pk)]))
    return HttpResponseRedirect(reverse_lazy('home'))


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

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        blogpost = self.object

        if self.request.user.is_authenticated:
            context['has_liked'] = blogpost.likes.filter(id=self.request.user.id).exists()
        else:
            context['has_liked'] = False

        return context  

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
