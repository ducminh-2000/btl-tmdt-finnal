from django.shortcuts import render

from shop.models import *



# ------------------------------ PRODUCT ---------------------------------


def render_list(request, category):
    if int(category) == 1:
        products = BookItem.objects.all()
        return render(request, "product/list.html", {'products': products, "category": 1})
    elif int(category) == 2:
        products = LaptopItem.objects.all()
        return render(request, "product/list.html", {'products': products, "category": 2})
    elif int(category) == 3:
        products = ClothesItem.objects.all()
        return render(request, "product/list.html", {'products': products, "category": 3})
    elif int(category) == 4:
        products = MobilePhoneItem.objects.all()
        return render(request, "product/list.html", {'products': products, "category": 4})


def render_product(request):
    books = BookItem.objects.all()
    return render(request, "product/list.html", {'products': books, "category": 1})


def render_detail(request, id, category):
    if int(category) == 1:
        product = BookItem.objects.get(pk=id)
        return render(request, "product/detail.html", {'product': product, "category":1})
    elif int(category) == 2:
        product = LaptopItem.objects.get(pk=id)
        return render(request, "product/detail.html", {'product': product, "category":2})
    elif int(category) == 3:
        product = ClothesItem.objects.get(pk=id)
        return render(request, "product/detail.html", {'product': product, "category":3})
    elif int(category) == 4:
        product = MobilePhoneItem.objects.get(pk=id)
        return render(request, "product/detail.html", {'product': product, "category":4})
