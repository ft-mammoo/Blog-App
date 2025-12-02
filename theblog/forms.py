from django import forms
from .models import BlogPost, Category
import bleach


def get_category_choices():
    return Category.objects.all().values_list('id', 'name')

ALLOWED_TAGS = [
    'p', 'br', 'strong', 'em', 'u', 'ol', 'ul', 'li', 'blockquote', 'h1', 'h2', 'h3',
    'a', 'img', 'pre', 'code', 'span', 'div'
]
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title', 'target'],
    'img': ['src', 'alt', 'width', 'height'],
    'span': ['style'], 
    'div': ['class']
}


class BlogPostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.choices = get_category_choices()

    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'category', 'content', 'snippet']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter title tag here'}),
            #'author' : forms.TextInput(attrs={'class' : 'form-control', 'id' : 'authorid', 'value' : '', 'type' : 'hidden'}),
            'category' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Select category'}),
            'snippet' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter a brief snippet about the post'}),
        }
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content:
            sanitized_content = bleach.clean(
                content,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                strip=True
            )
            return sanitized_content
        return content

class EditBlogPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.choices = get_category_choices()
        
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'category', 'content', 'snippet']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter title tag here'}),
            'category' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Select category'}),
            'snippet' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter a brief snippet about the post'}),
        }
        
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content:
            sanitized_content = bleach.clean(
                content,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                strip=True
            )
            return sanitized_content
        return content