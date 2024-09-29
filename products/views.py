from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q 
from products.models import Category,Product
from products.forms import CategoryForm, ProductForm


class CreateCategoryProduct(View):
    def get(self, request, *args, **kwargs):
        category_form = CategoryForm()
        product_form = ProductForm()
        categories = Category.objects.all()

        query = self.request.GET.get('q')

        if query:
             products = Product.objects.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query)
            )
        else:
            products =Product.objects.all()

        context = {
            'category_form': category_form,
            'categories': categories,
            'product_form': product_form,
            'products': products,
            'update': False,
            'index': False,
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
            'update': False,
            'index': False,
        }
        return render(request, 'core/dashboard.html', context)


class DeleteCategory(View):
    def post(self, request, cat_id):
        category = get_object_or_404(Category, id=cat_id)
        category.delete()
        return redirect('products:dashboard')


class DeleteProduct(View):
    def post(self, request, pro_id):
        product = get_object_or_404(Product, id=pro_id)
        product.delete()
        return redirect('products:dashboard')
    

class UpdateProduct(View):
    def get(self, request, pro_id):
        product = get_object_or_404(Product, id=pro_id)
        product_form = ProductForm(instance=product)
        category_form = CategoryForm()
        categories = Category.objects.all()
        products = Product.objects.all()

        context = {
            'product_form': product_form,
            'category_form': category_form,
            'categories': categories,
            'products': products,
            'update': True,
            'index': False,
        }

        return render(request, 'core/dashboard.html', context)


    def post(self, request, pro_id):
        product = get_object_or_404(Product, id=pro_id)
        product_form = ProductForm(request.POST, request.FILES, instance=product)

        if product_form.is_valid():
            product_form.save()
            return redirect('products:dashboard')
        
        category_form = CategoryForm()
        categories = Category.objects.all()
        products = Product.objects.all()
        
        context = {
            'product_form': product_form,
            'category_form': category_form,
            'categories': categories,
            'products': products,
            'update': True
        }

        return render(request, 'core/dashboard.html', context)


class MainPage(View):

    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
            'categories': categories,
            'products': products,
            'index': True,
        }

        return render(request, 'products/index.html', context)

