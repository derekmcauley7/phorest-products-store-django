from django.shortcuts import render
from userprofile.models import Profile
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from phorestapi.phorestapi import PhorestApi
from order.order_builder import OrderBuilder

@login_required(login_url= "/login")
def order_complete(request):
    order = OrderBuilder.create_order(request)

    response = PhorestApi.create_purchase(order)
    clear_cart(request)
    
    user_profile = Profile.objects.get(user = order.user)
    return render(request, "order/order-complete.html", {"order" : order, "profile" : user_profile})

def clear_cart(request):
    Cart(request).clear()


        



