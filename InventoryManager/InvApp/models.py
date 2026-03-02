from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0)
    qty = models.IntegerField(default=0)
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.product_id