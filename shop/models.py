from django.db import models
from django.contrib.auth.models import User



#  -------------------------- CUSTOMER ------------------------------------


class Customer(models.Model):
    user = models.OneToOneField(User,related_name="customer_profile", on_delete=models.CASCADE, null=True, blank=True)
    GENDER_CHOICES = (('M', 'Nam'), ('F', 'Nữ'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, default='')

    USERNAME_FIELD = 'full_name'

    def __str__(self):
        return self.user.email




# -------------------------- PRODUCT -----------------------------------


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


    #  -------------------------- CART -------------------------------


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




# ---------------------------- PAYMENT AND SHIPMENT -------------------------------

class Payment(models.Model):
    method = models.CharField(max_length=200)
    totalamount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

class Shipment(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    method = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)



#  ----------------------------- ORDER ----------------------------------

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




