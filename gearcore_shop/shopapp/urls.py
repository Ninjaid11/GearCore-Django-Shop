from django.urls import path
from .views import index, product_search, product_by_brand, products_by_category, account_info, \
    order_history, my_returns, account_dashboard, change_password, product_detail, add_to_cart, cart_detail, cart_plus, \
    cart_minus, cart_remove, order

urlpatterns = [
    path('', index, name='index'),
    path('product/<str:product_name>/', product_detail, name='product_detail'),
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('cart/plus/<int:item_id>/', cart_plus, name='cart_plus'),
    path('cart/minus/<int:item_id>/', cart_minus, name='cart_minus'),
    path('cart/remove/<int:item_id>/', cart_remove, name='cart_remove'),
    path('order/', order, name="order"),
    path('search', product_search, name='product_search'),
    path('category/<str:category_name>/', products_by_category, name='products_by_category'),
    path('brand/<str:brand_name>/',   product_by_brand, name='product_by_brand'),
    path('profile/', account_dashboard, name='account_dashboard'),
    path('profile/account-info/', account_info, name='account_info'),
    path('profile/orders/', order_history, name='order_history'),
    path('profile/returns/', my_returns, name='my_returns'),
    path('account/password/change/', change_password, name='change_password')
]