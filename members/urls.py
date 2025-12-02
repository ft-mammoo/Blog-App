from django.urls import path
from .views import SignUpView, EditProfileView, PasswordsChangeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
]
