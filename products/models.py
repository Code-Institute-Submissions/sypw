from django.db import models


class Payslip(models.Model):
    name = models.CharField(max_length=254)
    ni = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    def get_ni(self):
        return self.ni


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField
    price = models.DecimalField(max_digits=6, decimal_places=2)
    additional_info = models.CharField(max_length=254)

    def __str__(self):
        return self.name
