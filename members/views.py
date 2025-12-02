from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordsChangeForm
from django.contrib.auth.views import PasswordChangeView

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class EditProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')
