from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Brand, Category


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products': products})\

def product_search(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        error = "Пожалуйста, введите поисковый запрос."
        return render(request, "search.html", {'error': error})

    return render(request, "search.html", {'products': products, 'query': query})

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products_by_category.html', {
        'category': category,
        'products': products
    })

def product_by_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    products = Product.objects.filter(brand=brand)
    return render(request, 'product_by_brand.html', {
        'brand': brand,
        'products': products
    })