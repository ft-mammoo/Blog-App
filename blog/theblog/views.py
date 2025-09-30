from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

class HomePageView(ListView):
    model = BlogPost
    template_name = 'home.html'