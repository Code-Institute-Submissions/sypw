from django.db import models
from django.contrib.auth.models import User


class Payslip(models.Model):
    name = models.CharField(max_length=254)
    ni = models.CharField(max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_ni(self):
        return self.ni
