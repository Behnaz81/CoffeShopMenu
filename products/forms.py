from django import forms
from products.models import Category


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
    

