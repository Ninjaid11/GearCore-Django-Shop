from pyexpat.errors import messages

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.db.models import Q
from .models import Product, Brand, Category
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import LoginForm


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

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')