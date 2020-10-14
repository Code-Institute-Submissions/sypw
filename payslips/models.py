from django.db import models


class Payslip(models.Model):
    name = models.CharField(max_length=254)
    ni = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    def get_ni(self):
        return self.ni