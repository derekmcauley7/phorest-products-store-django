from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    total_price = models.DecimalField(max_digits=1000000, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def order_items(self):
        return OrderItem.objects.filter(order = self)

    def calculate_total(self):
        total = 0
        order_items = OrderItem.objects.filter(order = self)
        for item in order_items:
            total = total + Decimal(item.price) * Decimal(item.quantity)
        return total




class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orderItem")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    quantity = models.IntegerField()
