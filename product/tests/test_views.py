from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product


class TestViews(TestCase):

    def setUp(self):
        product = Product.objects.create(
            id = 1,
            name="test product",
            price = 20,
            quantityInStock = 1,
            image = 'http://someurl/someimage.png',
        )

    def test_product_list(self):
        client = Client()
        response = client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/products.html')
