from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem, Order, OrderItem,Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    category = request.GET.get('category')

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    return render(request, 'products/home.html', {
        'products': products,
        'selected_category': category,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(
        request,
        'products/product_detail.html',
        {'product': product}
    )


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        product=product
    )

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    return redirect('cart')
def cart(request):
    cart_items = CartItem.objects.all()

    total = sum(
        item.total_price()
        for item in cart_items
    )

    return render(
        request,
        'products/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )
def increase_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')


def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)

    cart_item.delete()

    return redirect('cart')
def checkout(request):
    cart_items = CartItem.objects.all()

    total = sum(
        item.total_price()
        for item in cart_items
    )

    return render(
        request,
        'products/checkout.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )
def place_order(request):
    cart_items = CartItem.objects.all()

    if not cart_items.exists():
        return redirect('cart')

    total = sum(
        item.total_price()
        for item in cart_items
    )

    order = Order.objects.create(
    customer_name=request.POST.get('customer_name'),
    phone=request.POST.get('phone'),
    address=request.POST.get('address'),
    total_amount=total,
    status='Pending'
)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return redirect('order_success')
def order_success(request):
    return render(request, 'products/order_success.html')
def my_orders(request):
    orders = Order.objects.all().order_by('-created_at')

    return render(
        request,
        'products/my_orders.html',
        {'orders': orders}
    )
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    items = OrderItem.objects.filter(order=order)

    return render(
        request,
        'products/order_detail.html',
        {
            'order': order,
            'items': items
        }
    )
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if order.status == 'Pending':
        order.status = 'Cancelled'
        order.save()

    return redirect('order_detail', order_id=order.id)
def cancel_order(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        if order.status == 'Pending':
            order.status = 'Cancelled'
            order.save()

    return redirect('my_orders')
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        order.status = "Cancelled"
        order.save()

    return redirect('my_orders')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'products/register.html', {
                'error': 'Passwords do not match.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'products/register.html', {
                'error': 'Username already exists.'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'products/register.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'products/login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'products/login.html')
def user_logout(request):
    logout(request)
    return redirect('home')