from .models import Brand, Product
from django import forms

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
        labels = {
            'name' : 'Brand Name'
        }
        widgets = {
            'name' : forms.TextInput(
                attrs={'class':'form-control'}
            )
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Name',
            'sku' : 'SKU',
            'price' : 'Price',
            'qty' : 'Quantity',
            'brand' : 'Brand',
        }
        widgets = {
            'name' : forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'sku' : forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'price' : forms.NumberInput(
                attrs={'class':'form-control'}
            ),
            'qty' : forms.NumberInput(
                attrs={'class':'form-control'}
            ),
            'brand' : forms.Select(
                attrs={'class':'form-select'}
            )
        }