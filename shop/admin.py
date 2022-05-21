from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'publicationdate', 'numberofpage')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'description',
                    'numberSold', 'numAvailidInStock')


admin.site.register(Book, BookAdmin)
admin.site.register(BookItem, ItemAdmin)
admin.site.register(Author)
admin.site.register(Publisher)


# ---------------------------------------------------Laptop---------------------------------------------------
class LaptopAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'ram', 'brand', 'brand',
        'battery',
        'weight',
        'material',
        'warranty',
        'size',
        'operationSystem'
    )


class CPUAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'techType',
        'typeCpu',
        'speed',
        'brand'
    )


class VGAAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'vram',
        'tech',
        'brand',
    )


admin.site.register(Laptop, LaptopAdmin)
admin.site.register(LaptopItem, ItemAdmin)
admin.site.register(Producer)
admin.site.register(CPU, CPUAdmin)
admin.site.register(VGA, VGAAdmin)


# -------------------------------------Clothes-----------------------------------------------------------------

admin.site.register(CategoryClothes)
admin.site.register(Clothes)
admin.site.register(ClothesItem, ItemAdmin)

# --------------------------------------MobilePhone---------------------------------------------------------

admin.site.register(MobilePhone)
admin.site.register(MobilePhoneItem, ItemAdmin)


admin.site.register(Cart)
admin.site.register(CartBookItem)
admin.site.register(CartLaptopItem)
admin.site.register(CartClothesItem)
admin.site.register(CartMobilePhoneItem)

admin.site.register(Order)
admin.site.register(Voucher)

admin.site.register(Payment)

admin.site.register(Shipment)

