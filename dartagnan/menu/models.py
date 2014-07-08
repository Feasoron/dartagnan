from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    Description = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=5, decimal_places=2)
