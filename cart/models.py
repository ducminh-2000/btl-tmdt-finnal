from django.db import models

# Create your models here.
from customer.models import Customer
from products.models import BookItem, LaptopItem, MobilePhoneItem, ClothesItem


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quanity = models.DecimalField(max_digits=10, decimal_places=0,null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=0,default=0)
    state = models.BooleanField(default=False)


class CartBookItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    bookItem = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class CartLaptopItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    laptopItem = models.ForeignKey(LaptopItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


class CartMobilePhoneItem(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    mobilephoneItem = models.ForeignKey(MobilePhoneItem, on_delete=models.CASCADE)


class CartClothesItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    clothesItem = models.ForeignKey(ClothesItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)