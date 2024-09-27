from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views import View
from core.forms import LoginForm

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True
    login_url = '/login/'
    form_class = LoginForm
    
    def get_success_url(self):
        return reverse_lazy('products:dashboard')
    