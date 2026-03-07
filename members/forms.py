from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from theblog.models import Profile
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class ProfileSettingsForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    is_staff = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    last_login = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password', 'is_staff', 'is_active','is_superuser', 'date_joined', 'last_login')

class PasswordsChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class CreateProfilePageForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    website_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)
    facebook_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)
    x_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)
    instagram_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'x_url', 'instagram_url')

class EditProfilePageForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    website_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)
    facebook_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)
    x_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)
    instagram_url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'x_url', 'instagram_url')
