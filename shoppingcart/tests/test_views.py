from email.mime import image
from urllib import response
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from product.models import Product

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        product = Product.objects.create(
            id = 1,
            name="test product",
            price = 20,
            quantity_in_stock = 1,
            image = 'http://someurl/someimage.png',
        )
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)


    def test_add_cart_item_view(self):
        self.login_user()

        response = self.client.get(reverse('cart_add', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_clear_cart_should_redirect_view(self):
        response = self.client.get(reverse('item_clear', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_cart_details_view(self):
        self.login_user()

        response = self.client.get(reverse('cart_detail'))
        self.assertTemplateUsed('display-cart.html')
        self.assertEqual(response.status_code, 200)

    def login_user(self):
        return self.client.post('/login', self.credentials, follow=True)
