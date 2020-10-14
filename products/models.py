from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    additional_info = models.CharField(max_length=254)

    def __str__(self):
        return self.name
