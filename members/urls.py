from django.urls import path
from .views import SignUpView, EditProfileView, PasswordsChangeView, password_success

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', password_success.as_view(), name='password_success'),
]
