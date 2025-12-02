from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
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

class EditProfileForm(UserChangeForm):
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
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active','is_superuser', 'date_joined', 'last_login')
