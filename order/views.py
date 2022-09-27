from django.shortcuts import render
from product.models import Product
from userprofile.models import Profile
from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from decimal import Decimal
from django.conf import settings
from .models import Product
from phorestapi.phorestapi import PhorestApi

@login_required(login_url= "/login")
def order_complete(request):
    total_order_price = 0 
    order = Order.objects.create(total_price = total_order_price, user_id= request.user.id)
    cart = Cart(request)
    order.user = request.user
    order_items = []
    for key, value in request.session.get(settings.CART_SESSION_ID).items():
        product = Product.objects.get(pk=value['product_id'])
        total_order_price = total_order_price + Decimal(value['quantity']) * Decimal(value['price'])

        order_item = OrderItem.objects.create(
            price = Decimal(value['price']), 
            quantity = int(value['quantity']), 
            product = product,
            order = order)
        order_item.save()
        order_items.append(order_item)
    
    order.total_price = total_order_price
    order.save()
    profile = Profile.objects.get(user = order.user)
    cart.clear()
    
    return render(request, "order/order-complete.html", {"order" : order, "profile" : profile})


        



