from django.urls import path
from .views import HomePageView, ArticleDetailView, CreatePostView, EditPostView, DeletePostView, CreateCategoryView, CategoryView, LikeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('addpost/', CreatePostView.as_view(), name='create-post'),
    path('article/edit/<int:pk>/', EditPostView.as_view(), name='edit-post'), 
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete-post'),
    path('addcategory/', CreateCategoryView.as_view(), name='create-category'),
    path('category/<str:categs>/', CategoryView, name='category'),
    path('like/<int:pk>/', LikeView, name='like-post')
]
