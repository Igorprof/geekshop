from django.shortcuts import render
from mainapp.models import Product, ProductCategory

# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop - главная'
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'GeekShop - продукты',
        'categories': ProductCategory.objects.all(),
        'product_list': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', context)