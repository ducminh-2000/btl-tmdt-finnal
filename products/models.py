from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
# -------------------------------------------------------Book----------------------------------------


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=200, null=True, blank=True)
    publicationdate = models.CharField(max_length=200, null=True, blank=True)
    numberofpage = models.DecimalField(max_digits=10, decimal_places=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class BookItem(models.Model):
    # id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255, null=True) 
    price = models.FloatField()
    discount = models.FloatField()
    description = models.CharField(max_length=255, null=True) 
    numberSold = models.IntegerField(default=0)
    numAvailidInStock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/book/%Y/%m/%d', blank=True)

# -----------------------------------------------Clothes-------------------------------------------------------


class CategoryClothes(models.Model):
    type = models.TextField(blank=True)


class Clothes(models.Model):
    productName = models.CharField(max_length=255, null=True)  
    marterial = models.CharField(max_length=255,null=True)
    countryOfOrigin = models.CharField(max_length=255, null=True)  
    brand = models.CharField(max_length=255, null=True) 
    size = models.CharField(max_length=255, null=True)   
    importPrice = models.FloatField(default=0)
    color = models.CharField(max_length=255, null=True) 
    category = models.ForeignKey(CategoryClothes, on_delete=models.CASCADE)


class ClothesItem(models.Model):
    #  id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255, null=True) 
    price = models.FloatField()
    discount = models.FloatField()
    description = models.CharField(max_length=255, null=True) 
    numberSold = models.IntegerField(default=0)
    numAvailidInStock = models.IntegerField(default=0)
    images = models.ImageField(null=True, blank=True)
    clothes = models.ForeignKey(Clothes,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/clothes/%Y/%m/%d', blank=True)

# --------------------------------------------Laptop-------------------------------------------------------------------


class Producer(models.Model):
    name = models.CharField(max_length=200)

class VGA(models.Model):
    # id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255, null=True)   
    vram = models.CharField(max_length=255, null=True) 
    tech = models.CharField(max_length=255, null=True) 
    brand = models.CharField(max_length=255, null=True)   
    def __str__(self):
        return self.name
    # class Meta:
    #     db_table = "vga"

class CPU(models.Model):
    # id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255, null=True)   
    techType = models.CharField(max_length=255, null=True) 
    typeCpu = models.CharField(max_length=255, null=True)   
    speed = models.CharField(max_length=255, null=True) 
    brand = models.CharField(max_length=255, null=True)   
    def __str__(self):
        return self.name


class Laptop(models.Model):
    name = models.CharField(max_length=200)
    ram = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    battery = models.CharField(max_length=200, null=True, blank=True)
    weight = models.CharField(max_length=200, null=True, blank=True)
    material = models.CharField(max_length=200, null=True, blank=True)
    warranty = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    operationSystem = models.CharField(max_length=200, null=True, blank=True)
    vga = models.ForeignKey(VGA, on_delete=models.CASCADE,null=True, blank=True)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE,null=True, blank=True)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)


class LaptopItem(models.Model):
#    id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255, null=True) 
    price = models.FloatField()
    discount = models.FloatField()
    description = models.CharField(max_length=255, null=True) 
    numberSold = models.IntegerField(default=0)
    numAvailidInStock = models.IntegerField(default=0)
    laptop = models.ForeignKey(Laptop,on_delete=models.CASCADE,null=True,)
    image = models.ImageField(upload_to='products/laptop/%Y/%m/%d', blank=True)

# -------------------------------------------------MobilePhone---------------------------------------------------------------


class MobilePhone(models.Model):
    name = models.CharField(max_length=200)
    cpu = models.CharField(max_length=200, blank=True, null=True)
    screen = models.CharField(max_length=200, blank=True, null=True)
    ram = models.CharField(max_length=200, blank=True, null=True)
    feature = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    operation_system = models.CharField(max_length=200, blank=True, null=True)
    battery = models.CharField(max_length=200, blank=True, null=True)
    warranty = models.CharField(max_length=200, blank=True, null=True)
    backcamera = models.CharField(max_length=200, blank=True, null=True)
    fontcamera = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    size = models.CharField(max_length=200, blank=True, null=True)


class MobilePhoneItem(models.Model):
    # id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=255, null=True) 
    price = models.FloatField()
    discount = models.FloatField()
    description = models.CharField(max_length=255, null=True) 
    numberSold = models.IntegerField(default=0)
    numAvailidInStock = models.IntegerField(default=0)
    mobilePhone = models.ForeignKey(MobilePhone,on_delete=models.CASCADE,null=True,)
    image = models.ImageField(upload_to='products/mobilephone/%Y/%m/%d', blank=True)
