from django.urls import path
from .views import HomePageView, ArticleDetailView, CreatePostView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('addpost/', CreatePostView.as_view(), name='create-post'),
]
