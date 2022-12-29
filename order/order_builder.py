from product.models import Product
from order.models import Order, OrderItem
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
        for index, item in request.session.get(settings.CART_SESSION_ID).items():
            product = Product.objects.get(pk=item['product_id'])
            order_item = OrderItem.objects.create(
                price = Decimal(item['price']), 
                quantity = int(item['quantity']), 
                product = product,
                order = order)
            order_item.save()