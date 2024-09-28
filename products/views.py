from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from products.models import Category
from products.forms import CategoryForm


class CreateCategory(View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'core/dashboard.html', context)
    
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:dashboard')
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
        }
        return render(request, 'core/dashboard.html', context)
    

class DeleteCategory(View):
    def post(self, request, cat_id):
        category = get_object_or_404(Category, id=cat_id)
        category.delete()
        return redirect('products:dashboard')
