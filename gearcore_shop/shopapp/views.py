from xml.etree.ElementInclude import include

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


from .models import Product, Brand, Category, Comment, CartItem, Order
from  .forms import UserUpdateFrom, CommentForm, OrderForm


# Create your views here.

def index(request):
    products = Product.objects.all()
    brand = Brand.objects.all()
    return render(request, "index.html", {
        'products': products,
        'brands': brand
    })

def product_detail(request, product_name):
    product = get_object_or_404(Product, name__iexact=product_name)
    comments = Comment.objects.filter(product=product)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = Comment(
                user=request.user,
                product=product,
                content=comment_form.cleaned_data["content"]
            )
            new_comment.save()
            return redirect('product_detail', product_name=product.name)
    else:
        comment_form = CommentForm()

    return render(request, 'product_detail.html', {
        'product': product,
        'comments': comments,
        'comment_form': comment_form
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.count += 1
        cart_item.save()
    else:
        session_cart = request.session.get('cart', {}) # получаем корзину из сессии
        product_id_str = str(product_id)
        if product_id_str in session_cart:
            session_cart[product_id_str] += 1
        else:
            session_cart[product_id_str] = 1
        request.session['cart'] = session_cart # обновляет корзину в сессии
    return redirect('cart_detail')

def cart_detail(request):
    total_price = 0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            total_price += item.product.price * item.count
    else:
        session_cart = request.session.get('cart', {})
        cart_items = []

        for product_id_str, count in session_cart.items():
            product = get_object_or_404(Product, id=int(product_id_str))
            total_price += product.price * count
            cart_items.append({
                'product': product,
                'count': count,
                'total_price': product.price * count
            })

    return render(request, 'cart_item.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def cart_plus(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=item_id, user=request.user)
        item.count += 1
        item.save()
    else:
        session_cart = request.session.get('cart', {})
        product_id_str = str(item_id)

        if product_id_str in session_cart:
            session_cart[product_id_str] += 1
        else:
            session_cart[product_id_str] = 1
        request.session['cart'] = session_cart

    return redirect('cart_detail')

def cart_minus(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=item_id, user=request.user)
        if item.count > 1:
            item.count -= 1
            item.save()
        else:
            item.delete()
    else:
        session_cart = request.session.get('cart', {})
        product_id_str = str(item_id)

        if product_id_str in session_cart:
            if session_cart[product_id_str] > 1:
                session_cart[product_id_str] -= 1
            else:
                del session_cart[product_id_str]

        request.session['cart'] = session_cart

    return redirect('cart_detail')

def cart_remove(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=item_id, user=request.user)
        item.delete()
    else:
        session_cart = request.session.get('cart', {})
        product_id_str = str(item_id)

        if product_id_str in session_cart:
            del session_cart[product_id_str]

        request.session['cart'] = session_cart
    return redirect('cart_detail')

def order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for item in cart_items:
                order.products.add(item.product)
            cart_items.delete()

            message = render_to_string('emails/order_confirmation.txt', {
                'first_name': order.first_name,
                'last_name': order.last_name,
                'delivery_day': order.delivery_day,
                'phone': order.phone
            })
            send_mail(
                subject='Подтверждение заказа',
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[order.email],
                fail_silently=False
            )
            return redirect('/')
    else:
        if request.user.is_authenticated:
            initial_data = {
                'email': request.user.email
            }
            form = OrderForm(initial=initial_data)
        else:
            form = OrderForm()

    return render(request, 'order.html', {'form': form, 'cart_items': cart_items})


def product_search(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct() # чтобы избежать дубликатов
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
    if request.method == 'POST':
        form = UserUpdateFrom(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile/account-info/?success=true')
    else:
        form = UserUpdateFrom(instance=request.user)

    return render(request, 'profile/account_info.html', {'form': form})

@login_required
def address_book(request):
    return render(request, 'profile/address_book.html')

@login_required
def order_history(request):
    return render(request, 'profile/orders_history.html')

@login_required
def my_returns(request):
    return render(request, 'profile/my_returns.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password1')

        user = request.user

        if not user.check_password(old_password):
            return render(request, 'account/change_password.html', {'error': 'Старый пароль неверен'})

        if new_password1 != new_password2:
            return render(request, 'account/change_password.html', {'error': 'Пароли не совпадают'})

        if len(new_password1) < 8:
            return render(request, 'account/change_password.html', {'error': 'Пароль слишком короткий'})

        user.set_password(new_password1)
        user.save()

        update_session_auth_hash(request, user)

        return render(request, 'account/change_password.html', {'success': True})

    return render(request, 'account/change_password.html')