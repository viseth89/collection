from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sloth'),
    path('products/',views.products, name='products'),
    path('products/product/', views.productDetail, name='productDetail'),
]