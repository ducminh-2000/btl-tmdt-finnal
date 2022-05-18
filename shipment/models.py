from django.db import models

# Create your models here.
from payment.models import Payment


class Shipment(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    method = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)