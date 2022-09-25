from django.test import SimpleTestCase
from django.urls import reverse, resolve
from order.views import order_complete

class TestUrls(SimpleTestCase):

    def test_order_complete_url(self):
        url = reverse('order-complete')
        self.assertEqual(resolve(url).func, order_complete)