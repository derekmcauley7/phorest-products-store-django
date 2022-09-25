from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_product_list(self):
        client = Client()
        response = client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/products.html')
