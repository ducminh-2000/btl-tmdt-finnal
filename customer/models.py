from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    GENDER_CHOICES = (('M', 'Nam'), ('F', 'Nữ'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, default='')

    USERNAME_FIELD = 'full_name'

    def __str__(self):
        return self.user.email