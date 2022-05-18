from django.db import models

# Create your models here.
from cart.models import Cart


class Payment(models.Model):
    method = models.CharField(max_length=200)
    totalamount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)