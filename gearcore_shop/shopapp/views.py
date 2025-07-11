from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Product, Brand, Category


# Create your views here.

def index(request):
    products = Product.objects.all()
    brand = Brand.objects.all()
    return render(request, "index.html", {
        'products': products,
        'brands': brand
    })

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

def products_by_category(request, category_name):
    category = get_object_or_404(Category, name__iexact=category_name)
    products = Product.objects.filter(category=category)
    return render(request, 'products_by_category.html', {
        'category': category,
        'products': products
    })

def product_by_brand(request, brand_name):
    brand = get_object_or_404(Brand, name__iexact=brand_name)
    products = Product.objects.filter(brand=brand)
    return render(request, 'product_by_brand.html', {
        'brand': brand,
        'products': products
    })

@login_required
def account_dashboard(request):
    return render(request, 'profile/dashboard.html')

@login_required
def account_info(request):
    return render(request, 'profile/account_info.html')

@login_required
def address_book(request):
    return render(request, 'profile/addresses_book.html')

@login_required
def order_history(request):
    return render(request, 'profile/orders_history.html')

@login_required
def my_returns(request):
    return render(request, 'profile/my_returns.html')