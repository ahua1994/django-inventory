from django.db import models
from product.models import *
from django.contrib.auth.models import User

# Create your models here.


class Firm(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    image = models.TextField()

    def __str__(self):
        return self.name


class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    firm = models.ForeignKey(Firm, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    total = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Purchased {self.quantity} {self.brand} {self.product} for ${self.total} by {self.firm}'s {self.user}"


class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    total = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"Sold {self.quantity} {self.brand} {self.product} for ${self.total} to {self.user}"
