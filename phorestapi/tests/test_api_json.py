from django.test import TestCase
from django.contrib.auth.models import User
from product.models import Product
from phorestapi.phorestapi import PhorestApi
from order.models import Order, OrderItem

class TestAPI(TestCase):

    def setUp(self):
        self.product = Product.objects.create(name = 'prdocut_name', price = 10, product_id =1, quantity_in_stock =1)
        user = User.objects.create(username = "testuser", password ="userpass1")
        self.order = Order.objects.create(user = user)
        self.order_item = OrderItem.objects.create(order = self.order, price = self.product.price, quantity =1, product = self.product)
        self.order_item2 = OrderItem.objects.create(order = self.order, price = 20, quantity =1, product = self.product)

    def test_product_items_json(self):
        expected_product_json = [{"branchProductId": "1", "price": 10.00, "quantity": 1}, {"branchProductId": "1", "price": 20.00, "quantity": 1}]
        actual_product_json = PhorestApi.order_items_data(self.order.order_items)
        self.assertEquals(actual_product_json, expected_product_json)

    def test_should_create_purchase_json(self):
        expected_purchase_json = {"clientId":"QLbhb0lKCrKmQemqd6h7iA", "items": [{"branchProductId": "1", "price": 10.00, "quantity": 1}, {"branchProductId": "1", "price": 20.00, "quantity": 1}], "number": "11111", "payments": [{"amount": 20.0, "type": "CREDIT"}]}

        actual_purchase_json = PhorestApi.create_purchase_request_data(self.order.order_items, 20.00, "11111")
        self.assertEquals(actual_purchase_json, expected_purchase_json)
