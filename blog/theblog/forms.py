from django import forms
from .models import BlogPost, Category
from ckeditor.widgets import CKEditorWidget
import bleach

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

def choices():
    return Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices():
    choice_list.append(item)

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'author', 'category', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter title tag here'}),
            'author' : forms.TextInput(attrs={'class' : 'form-control', 'id' : 'authorid', 'value' : '', 'type' : 'hidden'}),
            'category' : forms.Select(choices=choice_list,attrs={'class' : 'form-control', 'placeholder' : 'Select category'}),
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
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        fields = ['title', 'title_tag', 'category', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter title tag here'}),
            'category' : forms.Select(choices=choice_list,attrs={'class' : 'form-control', 'placeholder' : 'Select category'}),
            #'content' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Write your content here'}),
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
