from django.urls import path
from products import views
from django.contrib.auth.decorators import login_required

app_name = 'products'

urlpatterns = [
    path('dashboard/', login_required(views.CreateCategory.as_view()), name='dashboard'),
    path('delete-cat/<int:cat_id>/', login_required(views.DeleteCategory.as_view()), name='delete-cat'),
]