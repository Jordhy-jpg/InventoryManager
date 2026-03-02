from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.PositiveIntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.name