from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'author', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter title tag here'}),
            'author' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Select author'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Write your content here'}),
        }