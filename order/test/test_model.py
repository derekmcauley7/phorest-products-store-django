from django.test import TestCase
from order.models import Order, OrderItem
from product.models import Product
from django.contrib.auth.models import User

class TestModel(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name = 'prdocut_name', price = 10, product_id = 1, quantity_in_stock = 1)
        user = User.objects.create(username = "testuser", password ="userpass1")
        self.order = Order.objects.create(user = user)
        self.order_item = OrderItem.objects.create(order = self.order, price = 10, quantity = 1, product = self.product)
        self.order.save()

    def test_order(self):
        self.assertEquals(self.order.order_items.count(), 1)
        self.assertEquals(self.order.order_items.first(), self.order_item)
        self.assertEquals(self.order.total_price, 10)
        self.assertEquals(self.order.order_items.first().product, self.product)


