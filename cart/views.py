from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from cart.models import Cart, CartBookItem, CartLaptopItem, CartClothesItem, CartMobilePhoneItem
from customer.models import Customer
from order.models import Order
from products.models import BookItem, LaptopItem, ClothesItem, MobilePhoneItem


def cart_add(request, id, category):
    if request.user.id != 'None':
        customer = Customer.objects.get(user_id=request.user.id)
        cart, _ = Cart.objects.get_or_create(state=False, customer=customer)
        # book---------------------------
        if int(category) == 1:
            bookItem = BookItem.objects.get(pk=id)
            cartBookItem, _ = CartBookItem.objects.get_or_create(bookItem=bookItem, cart=cart)
            cartBookItem.quantity = cartBookItem.quantity + 1
            cartBookItem.save()
        # laptop----------------------------------
        elif int(category) == 2:
            laptopItem = LaptopItem.objects.get(pk=id)
            cartLaptopItem, _ = CartLaptopItem.objects.get_or_create(laptopItem=laptopItem, cart=cart)
            cartLaptopItem.quantity = cartLaptopItem.quantity + 1
            cartLaptopItem.save()
        # clothes----------------------------------
        elif int(category) == 3:
            clothesItem = ClothesItem.objects.get(pk=id)
            cartClothesItem, _ = CartClothesItem.objects.get_or_create(clothesItem=clothesItem, cart=cart)
            cartClothesItem.quantity = cartClothesItem.quantity + 1
            cartClothesItem.save()
        # mobilephone------------------------------------------------------------------------
        elif int(category) == 4:
            mobilephoneItem = MobilePhoneItem.objects.get(pk=id)
            cartMobilephoneItem, _ = CartMobilePhoneItem.objects.get_or_create(mobilephoneItem=mobilephoneItem, cart=cart)
            cartMobilephoneItem.quantity = cartMobilephoneItem.quantity + 1
            cartMobilephoneItem.save()
        return redirect("cart:cart_detail")
    else:
        return redirect("customer:login")


def cart_remove(request, productid, cartid, category):
    cart = Cart.objects.get(pk=cartid)
    #book_______________________________________

    if int(category) == 1:
        bookItem = BookItem.objects.get(pk=productid)
        cartBookItem = CartBookItem.objects.get(bookItem= bookItem, cart = cart)
        cartBookItem.delete()
    #laptop______________________________________

    elif int(category) == 2:
        laptopItem = LaptopItem.objects.get(pk=productid)
        cartLaptopItem = CartLaptopItem.objects.get(laptopItem=laptopItem, cart=cart)
        cartLaptopItem.delete()
    # Clothes-------------------------------------------------------------

    elif int(category) == 3:
        clothesItem = ClothesItem.objects.get(pk=productid)
        cartClothesItem = CartClothesItem.objects.get(clothesItem=clothesItem, cart=cart)
        cartClothesItem.delete()
    # MObilePhone------------------------------------------------

    elif int(category) == 4:
        mobilephoneItem = MobilePhoneItem.objects.get(pk=productid)
        cartMobilephoneItem = CartMobilePhoneItem.objects.get(mobilephoneItem=mobilephoneItem, cart=cart)
        cartMobilephoneItem.delete()



    return redirect("cart:cart_detail")


def cart_add_quantity(request, productid, cartid, category):
    quanitity = int(request.GET['quantity'])
    if quanitity == 0:
        return cart_remove(request, productid, cartid, category)
    else:
        cart = Cart.objects.get(pk=cartid)
        # book-----------------------------------------------------------------
        if int(category) == 1:
            bookItem = BookItem.objects.get(pk=productid)
            cartBookItem = CartBookItem.objects.get(bookItem=bookItem, cart = cart)
            cartBookItem.quantity = quanitity
            cartBookItem.save()
        # laptop---------------------------------------------------------------
        elif int(category) == 2:
            laptopItem = LaptopItem.objects.get(pk=productid)
            cartLaptopItem, _ = CartLaptopItem.objects.get_or_create(laptopItem=laptopItem, cart=cart)
            cartLaptopItem.quantity = quanitity
            cartLaptopItem.save()
        # colthes----------------------------------------------------------------
        elif int(category) == 3:
            clothesItem = ClothesItem.objects.get(pk=productid)
            cartClothesItem, _ = CartClothesItem.objects.get_or_create(clothesItem= clothesItem, cart=cart)
            cartClothesItem.quantity = quanitity
            cartClothesItem.save()
        # mobilephone--------------------------------------------------------------------
        elif int(category) == 4:
            mobilephoneItem = MobilePhoneItem.objects.get(pk=productid)
            cartMobilephoneItem, _ = CartMobilePhoneItem.objects.get_or_create(mobilephoneItem=mobilephoneItem, cart=cart)
            cartMobilephoneItem.quantity = quanitity
            cartMobilephoneItem.save()
        return redirect("cart:cart_detail")


def cart_detail(request):
    items = []
    customer = Customer.objects.get(user_id=request.user.id)
    cart, _ = Cart.objects.get_or_create(state=False, customer=customer)
    # Book---------------------------------------------------------------------------------------

    cartBookItems = CartBookItem.objects.all().filter(cart=cart)
    [items.append({'product': cartItem.bookItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.bookItem.price * cartItem.quantity, 'category': 1}) for cartItem in cartBookItems]
    # laptop-------------------------------------------------------------------------------------

    cartLaptopItems = CartLaptopItem.objects.all().filter(cart=cart)
    [items.append({'product': cartItem.laptopItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.laptopItem.price * cartItem.quantity, 'category': 2}) for cartItem in
     cartLaptopItems]
    # Clothes---------------------------------------------------------------------------------------------
    cartClothesItems = CartClothesItem.objects.all().filter(cart=cart)
    [items.append({'product': cartItem.clothesItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.clothesItem.price * cartItem.quantity, 'category': 3}) for cartItem in
     cartClothesItems]
    # Moiblephone-------------------------------------------------------------------------------------------
    cartMobilephoneItems = CartMobilePhoneItem.objects.all().filter(cart=cart)
    [items.append({'product': cartItem.mobilephoneItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.mobilephoneItem.price * cartItem.quantity, 'category': 4}) for cartItem in
     cartMobilephoneItems]

    cart.total_price = sum([item['totalprice'] for item in items])
    cart.quanity = sum([item['quanity'] for item in items])
    cart.save()
    return render(request, "cart/cart_detail.html", {"items": items, "cart": cart})
