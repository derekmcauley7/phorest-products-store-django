from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_order_complete_requires_login(self):
        self.client = Client()
        response = self.client.get(reverse('order-complete'))
        self.assertEqual(response.status_code, 302)

    def test_order_complete_with_login(self):
        # login User
        response = self.client.post('/login', self.credentials, follow=True)
        response = self.client.get(reverse('order-complete'))
        self.assertEqual(response.status_code, 200)

