from email.mime import image
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        product = Product.objects.create(
            id = 1,
            name="test product",
            price = 20,
            quantityInStock = 1,
            image = 'http://someurl/someimage.png',
        )


    def test_add_cart_item_view(self):
        response = self.client.get(reverse('cart_add', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_clear_cart_should_redirect_view(self):
        response = self.client.get(reverse('item_clear', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_cart_details_view(self):
        response = self.client.get(reverse('cart_detail'))
        self.assertTemplateUsed('display-cart.html')
        self.assertEqual(response.status_code, 200)
