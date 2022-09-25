from django.test import SimpleTestCase
from django.urls import reverse, resolve
from userprofile.views import register, LogoutInterfaceView, LoginInterfaceView

class TestUrls(SimpleTestCase):

    def test_register_view(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, register)

    def test_logout_view(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutInterfaceView)

    def test_login_view(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, LoginInterfaceView)