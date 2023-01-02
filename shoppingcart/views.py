from django.shortcuts import render, redirect
from phorestproducts.settings import STRIPE_PUBLISHABLE_KEY
from product.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from decimal import Decimal
from django.conf import settings

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("products")

def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect('shopping-cart:cart_detail')

def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('shopping-cart:cart_detail')

def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('shopping-cart:cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("display-cart.html")

@login_required(login_url= "/login", )
def cart_detail(request):
    cart = Cart(request)
    total = getTotal(request)
    key = STRIPE_PUBLISHABLE_KEY
    return render(request, 'shoppingcart/display-cart.html', {'total' : total, 'payment_amount' : total * 100 })

def getTotal(request):
    total = 0 
    for index, item in request.session.get(settings.CART_SESSION_ID).items():
        total = total + Decimal(item['quantity']) * Decimal(item['price'])
    return total