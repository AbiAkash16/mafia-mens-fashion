from django import views
from django.urls import path
from . views import (
    home,
    product_detail,
    add_to_cart,
    cart,
    increase_quantity,
    decrease_quantity,
    remove_from_cart,
    checkout,
    place_order,
    order_success,
    my_orders,
    order_detail,
    cancel_order,
    register,
    user_login,
    user_logout,

)

urlpatterns = [
    path('', home, name='home'),
    path("product/<int:product_id>/", product_detail, name="product_detail"),

    path(
        'product/<int:product_id>/',
        product_detail,
        name='product_detail'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        cart,
        name='cart'
    ),

    path(
        'cart/increase/<int:item_id>/',
        increase_quantity,
        name='increase_quantity'
    ),

    path(
        'cart/decrease/<int:item_id>/',
        decrease_quantity,
        name='decrease_quantity'
    ),

    path(
        'cart/remove/<int:item_id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),
    path(
    'checkout/',
    checkout,
    name='checkout'
),
    path(
        'place-order/',
        place_order,
        name='place_order'
    ),
    path(
    'order-success/',
    order_success,
    name='order_success'
),
    path(
        'my-orders/',
        my_orders,
        name='my_orders'
    ),
    path(
        'order/<int:order_id>/',
        order_detail,
        name='order_detail'
    ),
path(
    'cancel-order/<int:order_id>/',
    cancel_order,
    name='cancel_order'
),
path('register/', register, name='register'
     ),
path('login/', user_login, name='login'
     ),    
     path('logout/', user_logout, name='logout'),

]
from django.urls import path
from .views import (
    home,
    product_detail,
    add_to_cart,
    cart,
    increase_quantity,
    decrease_quantity,
    remove_from_cart,
    checkout,
    place_order,
    order_success,
    my_orders,
    order_detail,
    cancel_order,
    register,
    user_login,
    user_logout,
)