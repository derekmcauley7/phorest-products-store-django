from django.shortcuts import render
from .models import Product
from phorestapi.phorestapi import PhorestApi

def all_products(request):
  products = Product.objects.filter(price__gt = 0.00).filter(quantity_in_stock__gt = 0)
  if not products:
    productJson = PhorestApi.get_products()
    create_products(productJson)
  products = Product.objects.filter(price__gt = 0.00).filter(quantity_in_stock__gt = 0)
  return render(request, "product/products.html", {"products": products})

def create_products(productJson):
  default_image_url = "https://st.depositphotos.com/1987177/3470/v/450/depositphotos_34700099-stock-illustration-no-photo-available-or-missing.jpg"
  for product in productJson:
    newProduct = Product.objects.create(name = product["name"], price = product["price"], product_id=product["productId"], image=default_image_url, quantity_in_stock = product["quantityInStock"])
    newProduct.save()