from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
        'placeholder': 'نام کاربری',
        'class': 'form-control mx-auto w-75',
    }))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
        'placeholder': 'رمز عبور',
        'class': 'form-control mx-auto w-75',
    }))

