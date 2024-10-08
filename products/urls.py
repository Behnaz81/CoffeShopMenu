from django.urls import path
from products import views
from django.contrib.auth.decorators import login_required

app_name = 'products'

urlpatterns = [
    path('dashboard/', login_required(views.CreateCategoryProduct.as_view()), name='dashboard'),
    path('delete-cat/<int:cat_id>/', login_required(views.DeleteCategory.as_view()), name='delete-cat'),
    path('delete-product/<int:pro_id>/', login_required(views.DeleteProduct.as_view()), name='delete-product'),
    path('update-product/<int:pro_id>/', login_required(views.UpdateProduct.as_view()), name='update-product'),
    path('', views.MainPage.as_view(), name='index'),
]