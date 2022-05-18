from django.db import models

# Create your models here.
from cart.models import Cart
from customer.models import Customer
from payment.models import Payment
from shipment.models import Shipment

class Voucher(models.Model):
    # id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255)
    discountPercent = models.FloatField()
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Order(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    totalamount = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    note = models.CharField(max_length=200, null=True, blank=True)
    address_second = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    voucher = models.ManyToManyField(Voucher, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    STATE_CHOICES = (('0', 'Chờ xác nhận'), ('1', 'Đã xác nhận'),
                     ('2', 'Đang giao hàng'), ('3', 'Giao hàng thành công'), ('4', 'Huỷ'), ('5', 'Giao hàng thất bại'))
    state = models.CharField(max_length=1, choices=STATE_CHOICES, blank=True, default='0')