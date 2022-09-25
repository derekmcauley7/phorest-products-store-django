from django.urls import path

from . import views

urlpatterns = [      
    path('order/complete', views.order_complete, name = 'order-complete'),
]