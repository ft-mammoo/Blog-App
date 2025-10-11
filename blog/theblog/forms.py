from django import forms
from .models import BlogPost, Category

def choices():
    return Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices():
    choice_list.append(item)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'author', 'category', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter title tag here'}),
            'author' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Select author'}),
            'category' : forms.Select(choices=choice_list,attrs={'class' : 'form-control', 'placeholder' : 'Select category'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Write your content here'}),
        }

class EditBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'category', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter title tag here'}),
            'category' : forms.Select(choices=choice_list,attrs={'class' : 'form-control', 'placeholder' : 'Select category'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Write your content here'}),
        }