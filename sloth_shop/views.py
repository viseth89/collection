from django.shortcuts import render

def index(request):
    return render(request, 'sloth_shop/index.html')

def products(request):
    return render(request, 'sloth_shop/products.html')

def productDetail(request):
    return render(request, 'sloth_shop/product_detail.html')