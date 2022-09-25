from django.urls import path

from . import views

urlpatterns = [
    path('login', views.LoginInterfaceView.as_view(), name = 'login'),
    path('logout', views.LogoutInterfaceView.as_view(), name = 'logout'),
    path('signup', views.register, name = 'signup'),
    path("profile", views.update_profile, name='profile'),
]