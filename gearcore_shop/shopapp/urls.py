from django.urls import path
from .views import index, product_search, product_by_brand, products_by_category, account_info, address_book, \
    order_history, my_returns, account_dashboard

urlpatterns = [
    path('', index, name='index'),
    path('search', product_search, name='product_search'),
    path('category/<str:category_name>/', products_by_category, name='products_by_category'),
    path('brand/<str:brand_name>/',   product_by_brand, name='product_by_brand'),
    path('profile/', account_dashboard, name='account_dashboard'),
    path('profile/account-info/', account_info, name='account_info'),
    path('profile/addresses/', address_book, name='address_book'),
    path('profile/orders/', order_history, name='order_history'),
    path('profile/returns/', my_returns, name='my_returns'),
]