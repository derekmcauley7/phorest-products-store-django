from email.mime import image
from hashlib import new
from modulefinder import Module
from django.shortcuts import render

from phorestproducts.settings import API_ENDPOINT, API_USERNAME, API_PASSWORD
from .models import Product
from requests.auth import HTTPBasicAuth 
import requests

def all_products(request):
   products = Product.objects.filter(price__gt = 0.00)
   if not products.exists():
     productJson = make_api_request_for_products()
     create_products(productJson)
     products = Product.objects.filter(price__gt = 0.00)
   return render(request, "product/products.html", {"products": products})

def make_api_request_for_products():
    res = requests.get(API_ENDPOINT + 'product', 
    auth=HTTPBasicAuth(API_USERNAME, API_PASSWORD))
    return res.json().get('_embedded').get('products')

def create_products(productJson):
  for product in productJson:
        newProduct = Product.objects.create(name = product["name"], price = product["price"], productId=product["productId"], image="https://st.depositphotos.com/1987177/3470/v/450/depositphotos_34700099-stock-illustration-no-photo-available-or-missing.jpg", quantityInStock = product["quantityInStock"])
        newProduct.save()