from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)


    def test_user_login(self):
        response = self.client.post('/login', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_login_url(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/login.html')

    def test_logout_url(self):
        client = Client()
        response = client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/logout.html')

    def test_register_url(self):
        client = Client()
        response = client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/register.html')

    def test_profile_redirect_when_user_login_required(self):
        client = Client()
        response = client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_with_user_login(self):
        # login a user
        self.client = Client()
        response = self.client.post('/login', self.credentials, follow=True)

        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)