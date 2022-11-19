from urllib import response
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
    order = Order.objects.create(total_price = 0, user_id= request.user.id)
    cart = Cart(request)
    order.user = request.user
    create_order_items(request, order)
    
    order.total_price = order.calculate_total
    order.save()
    profile = Profile.objects.get(user = order.user)
    response = PhorestApi.create_purchase(order)
    cart.clear()
    
    return render(request, "order/order-complete.html", {"order" : order, "profile" : profile})

def create_order_items(request, order):
    for key, value in request.session.get(settings.CART_SESSION_ID).items():
        product = Product.objects.get(pk=value['product_id'])
        order_item = OrderItem.objects.create(
            price = Decimal(value['price']), 
            quantity = int(value['quantity']), 
            product = product,
            order = order)
        order_item.save()


        



