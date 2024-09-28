from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from products.models import Category,Product
from products.forms import CategoryForm, ProductForm


class CreateCategory(View):
    def get(self, request, *args, **kwargs):
        category_form = CategoryForm()
        product_form = ProductForm()
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
            'category_form': category_form,
            'categories': categories,
            'product_form': product_form,
            'products': products,
        }
        return render(request, 'core/dashboard.html', context)
    
    def post(self, request):
        category_form = CategoryForm()
        product_form = ProductForm()

        if request.POST.get('create') == 'category':
            category_form = CategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return redirect('products:dashboard')

        elif request.POST.get('create') == 'product':
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product_form.save()
                return redirect('products:dashboard')
            
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
            'category_form': category_form,
            'categories': categories,
            'product_form': product_form,
            'products': products,
        }
        return render(request, 'core/dashboard.html', context)


class DeleteCategory(View):
    def post(self, request, cat_id):
        category = get_object_or_404(Category, id=cat_id)
        category.delete()
        return redirect('products:dashboard')
