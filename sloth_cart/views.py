from django.shortcuts import render

def cart(request):
    return render(request, 'sloth_cart/cart.html')