from django.contrib import admin

# Register your models here.
from products.models import Book, Author, Publisher, BookItem, Laptop, LaptopItem, Producer, CategoryClothes, Clothes, \
    ClothesItem, MobilePhone, MobilePhoneItem, CPU, VGA

# -----------------------------------------------Book----------------------------


admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(Author)
admin.site.register(Publisher)


# ---------------------------------------------------Laptop---------------------------------------------------

admin.site.register(Laptop)
admin.site.register(LaptopItem)
admin.site.register(Producer)
admin.site.register(CPU)
admin.site.register(VGA)


# -------------------------------------Clothes-----------------------------------------------------------------

admin.site.register(CategoryClothes)
admin.site.register(Clothes)
admin.site.register(ClothesItem)

# --------------------------------------MobilePhone---------------------------------------------------------

admin.site.register(MobilePhone)
admin.site.register(MobilePhoneItem)