from django.shortcuts import render, redirect
from .models import Brand, Product
from .forms import BrandForm, ProductForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'InvApp/home.html', {'products':products})

def createBrand(request):
    form = BrandForm()

    if request.method == 'POST':
        form = BrandForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('createProduct')
    
    return render(request, 'InvApp/createBrand.html', {'form':form})

def createProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'InvApp/createProduct.html', {'form':form})