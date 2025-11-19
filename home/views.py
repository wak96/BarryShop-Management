from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def settings(request):
    return render(request, 'pages/settings.html')

def product(request):
    return render(request, 'pages/product.html')

def order(request):
    return render(request, 'pages/orders.html')

def inventory(request):
    return render(request, 'pages/inventory.html')

def customers(request):
    return render(request, 'pages/customers.html')

def categories(request):
    return render(request, 'pages/categories.html')

def barcode(request):
    return render(request, 'pages/barcode_manager.html')
