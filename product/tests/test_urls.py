from django.test import SimpleTestCase
from django.urls import reverse, resolve
from product.views import all_products

class TestUrls(SimpleTestCase):

    def test_list_products_urls(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func, all_products)