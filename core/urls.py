from django.urls import path
from core import views
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('dashboard/', login_required(views.Dashboard.as_view()), name='dashboard'),
]