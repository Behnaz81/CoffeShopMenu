from django import forms
from products.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        fields = ['name']
        model = Category

        labels = {
            'name': 'عنوان',
        }

        error_messages = {
            'name': {
                'required': 'لطفا یک نام وارد کنید.',
                'max_length': 'طول این نام می‌تواند حداکثر 255 کاراکتر باشد.',
                'unique': "این دسته بندی وجود دارد.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].label_classes = ('form-label')
    

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'image']

        labels = {
            'name': 'نام',
            'price': 'قیمت',
            'category': 'دسته‌بندی',
            'image': 'تصویر',
        }

        error_messages = {
            'name': {
                'required': 'لطفا یک نام وارد کنید.',
                'max_length': 'طول این نام می‌تواند حداکثر 255 کاراکتر باشد.',
                'unique': "محصولی با این نام وجود دارد.",
            },

            'price': {
                'required': 'لطفا قیمت را وارد کنید.',
            },

            'category': {
                'required': 'لطفا دسته‌بندی را انتخاب کنید.',
            },
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].label_classes = ('form-label')
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].label_classes = ('form-label')
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].label_classes = ('form-label')
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].label_classes = ('form-label')