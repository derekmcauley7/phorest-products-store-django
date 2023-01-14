from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=500, decimal_places=2)
    image = models.ImageField(upload_to='products/', max_length=500)
    product_id = models.TextField()
    quantity_in_stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
