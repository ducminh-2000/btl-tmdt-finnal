from django.contrib import admin

# Register your models here.
from cart.models import Cart, CartBookItem, CartLaptopItem, CartClothesItem, CartMobilePhoneItem

admin.site.register(Cart)
admin.site.register(CartBookItem)
admin.site.register(CartLaptopItem)
admin.site.register(CartClothesItem)
admin.site.register(CartMobilePhoneItem)