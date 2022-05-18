from django.urls import path

from . import views

urlpatterns = [
    path('cart_add/<id>/<category>', views.cart_add, name='cart_add'),
    path('cart_remove/<productid>/<cartid>/<category>', views.cart_remove, name='cart_remove'),
    path('cart_add_quantity/<productid>/<cartid>/<category>', views.cart_add_quantity, name='cart_add_quantity'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
]