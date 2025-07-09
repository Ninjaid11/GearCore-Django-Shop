from django.urls import path
from .views import index, product_search, product_by_brand, products_by_category

urlpatterns = [
    path('', index, name='index'),
    path('search', product_search, name='product_search'),
    path('category/<str:category_name>/', products_by_category, name='products_by_category'),
    path('brand/<str:brand_name>/',   product_by_brand, name='product_by_brand'),
]