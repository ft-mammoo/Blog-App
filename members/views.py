from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordsChangeForm
from django.contrib.auth.views import PasswordChangeView
from theblog.models import Profile

class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

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

class password_success(generic.TemplateView):
    template_name = 'registration/password_success.html'
