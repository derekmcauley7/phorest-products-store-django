from django.shortcuts import render
from .models import Product
from phorestapi.phorestapi import PhorestApi

def all_products(request):
   products = Product.objects.filter(price__gt = 0.00)
   if not products.exists():
     productJson = PhorestApi.get_products()
     create_products(productJson)
     products = Product.objects.filter(price__gt = 0.00)
   return render(request, "product/products.html", {"products": products})

def create_products(productJson):
  for product in productJson:
        newProduct = Product.objects.create(name = product["name"], price = product["price"], product_id=product["product_id"], image="https://st.depositphotos.com/1987177/3470/v/450/depositphotos_34700099-stock-illustration-no-photo-available-or-missing.jpg", quantity_in_stock = product["quantity_in_stock"])
        newProduct.save()