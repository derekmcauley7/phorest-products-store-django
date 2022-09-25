from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=1000000, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    productId = models.TextField()
    quantityInStock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
