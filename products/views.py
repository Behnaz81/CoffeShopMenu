from django.shortcuts import render, redirect
from django.views import View
from products.models import Category
from products.forms import CategoryForm


class CreateCategory(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'core/dashboard.html', {'form': form})
    
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:dashboard')
        return render(request, 'core/dashboard.html', {'form': form})
