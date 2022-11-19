from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shoppingcart.views import cart_add, item_increment, item_decrement, cart_clear, cart_detail

class TestUrls(SimpleTestCase):

    def test_add_to_cart_url(self):
        url = reverse('cart_add', args=[1])
        self.assertEqual(resolve(url).func, cart_add)
    
    def test_increment_cart_item_url(self):
        url = reverse('item_increment', args=[1])
        self.assertEqual(resolve(url).func, item_increment)   
    
    def test_decrement_cart_item_url(self):
        url = reverse('item_decrement', args=[1])
        self.assertEqual(resolve(url).func, item_decrement)  

    def test_clear_cart_url(self):
        url = reverse('cart_clear')
        self.assertEqual(resolve(url).func, cart_clear)  

    def test_cart_details_url(self):
        url = reverse('cart_detail')
        self.assertEqual(resolve(url).func, cart_detail)  