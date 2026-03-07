from django.urls import path
from .views import SignUpView, ProfileSettingsView, PasswordsChangeView, password_success, ShowProfilePageView, CreateProfilePageView, EditProfilePageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileSettingsView.as_view(), name='profile_settings'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success/', password_success.as_view(), name='password_success'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
]
