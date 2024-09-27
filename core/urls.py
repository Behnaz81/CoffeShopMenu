from django.urls import path
from core import views
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
]