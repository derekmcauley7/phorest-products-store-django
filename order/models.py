from django.db import models
from django.contrib.auth.models import User

from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    total_price = models.DecimalField(max_digits=1000000, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def order_items(self):
        return OrderItem.objects.filter(order = self)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orderItem")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order")
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    quantity = models.IntegerField()
