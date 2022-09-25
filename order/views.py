from django.shortcuts import render


from product.models import Product
from userprofile.models import Profile
from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from decimal import Decimal
from django.conf import settings
from phorestproducts.settings import API_ENDPOINT, API_USERNAME, API_PASSWORD
from .models import Product
from requests.auth import HTTPBasicAuth 
import requests

@login_required(login_url= "/login")
def order_complete(request):
    total = 0 
    order = Order.objects.create(totalPrice = total, user_id= request.user.id)
    cart = Cart(request)
    order.user = request.user
    orderItems = []
    for key, value in request.session.get(settings.CART_SESSION_ID).items():
        product = Product.objects.get(pk=value['product_id'])
        total = total + Decimal(value['quantity']) * Decimal(value['price'])

        orderItem = OrderItem.objects.create(
            price = Decimal(value['price']), 
            quantity = int(value['quantity']), 
            product = product,
            order = order)
        orderItem.save()
        orderItems.append(orderItem)
    
    order.totalPrice = total
    order.save()
    profile = Profile.objects.get(user = order.user)
    cart.clear()
    return render(request, "order/order-complete.html", {"order" : order, "profile" : profile})


def make_api_request_for_products():
    res = requests.post(API_ENDPOINT + 'purchase', 
    auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))
    return res.json().get('_embedded').get('products')


