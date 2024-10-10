from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    price = models.FloatField()
    currency = models.CharField(default="RUB", max_length=15)
    stock = models.IntegerField(default=0)
    image = models.CharField(max_length=2047, blank=True, null=True)

    def __str__(self):
        return self.name
