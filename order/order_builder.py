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


class OrderBuilder():
    def create_order(request):
        order = Order.objects.create(user = request.user)
        OrderBuilder.create_order_items(request, order)
        order.save()
        return order

    def create_order_items(request, order):
        for key, value in request.session.get(settings.CART_SESSION_ID).items():
            product = Product.objects.get(pk=value['product_id'])
            order_item = OrderItem.objects.create(
                price = Decimal(value['price']), 
                quantity = int(value['quantity']), 
                product = product,
                order = order)
            order_item.save()