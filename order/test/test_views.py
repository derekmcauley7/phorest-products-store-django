from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from order.models import Order, OrderItem, Product


class TestViews(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        user =User.objects.create_user(**self.credentials)
        self.product = Product.objects.create(name = 'prdocut_name', price = 10, product_id = 1, quantity_in_stock = 1)
        self.order = Order.objects.create(user = user)
        self.order_item = OrderItem.objects.create(order = self.order, price = 10, quantity = 1, product = self.product)
        self.order_item2 = OrderItem.objects.create(order = self.order, price = 20, quantity = 1, product = self.product)

    def test_order_complete_requires_login(self):
        self.client = Client()
        response = self.client.get(reverse('order-complete'))
        self.assertEqual(response.status_code, 302)

    def test_order_complete_with_login(self):
        # login User
        response = self.client.post('/login', self.credentials, follow=True)
        response = self.client.get(reverse('order-complete'))
        self.assertEqual(response.status_code, 200)

