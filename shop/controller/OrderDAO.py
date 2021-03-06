from django.shortcuts import redirect, render

from shop.models import *




#  -------------------------------- ORDER ----------------------------


def create_order(request):
    items = []
    customer = Customer.objects.get(user_id=request.user.id)
    cart = Cart.objects.get(state=False, customer=customer)
    # book-----------------------------------------------
    cartBookItems = CartBookItem.objects.all().filter(cart=cart)
    [items.append({'product': cartItem.bookItem, 'quanity': cartItem.quantity, 'totalprice': cartItem.bookItem.price * cartItem.quantity, 'category': 1}) for cartItem in cartBookItems]
    # laptop---------------------------------------------------------
    cartLaptopItems = CartLaptopItem.objects.all().filter(cart=cart)
    [items.append({'product': cartItem.laptopItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.laptopItem.price * cartItem.quantity, 'category': 2}) for cartItem in
     cartLaptopItems]
    # clothes---------------------------------------------------------------
    cartClothesItems = CartClothesItem.objects.all().filter(cart=cart)
    [items.append({'product': cartItem.clothesItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.clothesItem.price * cartItem.quantity, 'category': 3}) for cartItem in
     cartClothesItems]
    # mobilephone-----------------------------------------------------------
    cartMobilephoneItems = CartMobilePhoneItem.objects.all().filter(cart=cart)
    [items.append({'product': cartItem.mobilephoneItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.mobilephoneItem.price * cartItem.quantity, 'category': 4}) for cartItem in
     cartMobilephoneItems]
    return render(request, "orders/order_form.html", {"items": items, "cart": cart, "customer":customer})


def order_save(request):
    customer = Customer.objects.get(user_id=request.user.id)
    cart = Cart.objects.get(customer=customer, state=False)
    order = Order.objects.create(customer=customer)
    if cart.id != None:
        cart.state = True
        payment_type = request.POST['payment_type']
        payment,_ = Payment.objects.get_or_create(cart=cart)
        if int(payment_type) == 0:
            payment.method = "Thanh to??n khi nh???n h??ng"
        elif int(payment_type) == 1:
            payment.method = "Thanh to??n b???ng paypal"
        shipment_type = request.POST['shipment_type']
        shipment,_ = Shipment.objects.get_or_create(payment=payment)
        if int(shipment_type) == 0:
            shipment.method = "Giao h??ng ti??u chu???n"
            shipment.price = 3
        elif int(shipment_type) == 1:
            shipment.method = "Giao h??ng ti???t ki???m"
            shipment.price = 2
        elif int(shipment_type) == 2:
            shipment.method = "Giao h??ng nhanh"
            shipment.price = 4
        payment.save()
        shipment.save()
        order.payment = payment
        order.shipment = shipment
        order.totalamount = cart.total_price + shipment.price
        order.cart = cart
        cart.save()
        order.address_second = request.POST['address_second']
        order.save()
    return render(request, "orders/order_success.html")


def order_list(request):
    customer = Customer.objects.get(user_id=request.user.id)
    orders = Order.objects.all().filter(customer=customer)
    return render(request, "orders/order_list.html", {"orders":orders})


def order_detail(request, id):
    order = Order.objects.get(pk=id)
    items = []
    # Book---------------------------------------------------------------------------------------

    cartBookItems = CartBookItem.objects.all().filter(cart=order.cart)
    [items.append({'product': cartItem.bookItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.bookItem.price * cartItem.quantity, 'category': 1}) for cartItem in
     cartBookItems]
    # laptop-------------------------------------------------------------------------------------

    cartLaptopItems = CartLaptopItem.objects.all().filter(cart=order.cart)
    [items.append({'product': cartItem.laptopItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.laptopItem.price * cartItem.quantity, 'category': 2}) for cartItem in
     cartLaptopItems]
    # Clothes---------------------------------------------------------------------------------------------
    cartClothesItems = CartClothesItem.objects.all().filter(cart=order.cart)
    [items.append({'product': cartItem.clothesItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.clothesItem.price * cartItem.quantity, 'category': 3}) for cartItem in
     cartClothesItems]
    # Moiblephone-------------------------------------------------------------------------------------------
    cartMobilephoneItems = CartMobilePhoneItem.objects.all().filter(cart=order.cart)
    [items.append({'product': cartItem.mobilephoneItem, 'quanity': cartItem.quantity,
                   'totalprice': cartItem.mobilephoneItem.price * cartItem.quantity, 'category': 4}) for cartItem in
     cartMobilephoneItems]

    return render(request, "orders/order_detail.html", {"items": items, "order": order})


def order_remove(request, id):
    order = Order.objects.get(pk=id)
    order.state = 4
    order.save()
    return redirect("order_list")
