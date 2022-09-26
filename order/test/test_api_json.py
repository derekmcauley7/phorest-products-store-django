from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from product.models import Product
from order import views
from order.models import Order, OrderItem
from decimal import Decimal

class TestViews(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name = 'prdocut_name', price = 10, productId =1, quantityInStock =1)
        user = User.objects.create(username = "testuser", password ="userpass1")
        self.order = Order.objects.create(
            user = user,
            total_price = 10
        )
        self.order_item = OrderItem.objects.create(order = self.order, price = self.product.price, quantity =1, product = self.product)
        self.order_item2 = OrderItem.objects.create(order = self.order, price = 20, quantity =1, product = self.product)

    def test_product_items_json(self):
        expected_json = [{'branchProductId': '1', 'price': '10.00', 'quantity': 1}, {'branchProductId': '1', 'price': '20.00', 'quantity': 1}]
        product_json = views.order_items_data(self.order.order_items)
        self.assertEquals(product_json, expected_json)
