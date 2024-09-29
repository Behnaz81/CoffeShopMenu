from django.urls import path
from core import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView 

app_name = 'core'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', login_required(LogoutView.as_view()), name="logout"),
]