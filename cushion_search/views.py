from django.shortcuts import render
from cushion_shop.models import Product
from django.db.models import Q

def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query':query, 'products':products})