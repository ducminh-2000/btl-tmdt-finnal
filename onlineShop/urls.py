"""onlineShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.controller import CartDAO, CustomerDAO, OrderDAO, ProductDAO

urlpatterns = [
    path('admin/', admin.site.urls),

    # ---- CART ----
    path('cart_add/<id>/<category>', CartDAO.cart_add, name='cart_add'),
    path('cart_remove/<productid>/<cartid>/<category>', CartDAO.cart_remove, name='cart_remove'),
    path('cart_add_quantity/<productid>/<cartid>/<category>', CartDAO.cart_add_quantity, name='cart_add_quantity'),
    path('cart_detail/', CartDAO.cart_detail, name='cart_detail'),

    # ---- CUSTOMER ----
    path('', include('django.contrib.auth.urls')),
    path('signup/', CustomerDAO.signup, name='signup'),

    # ----- ORDER ------
    path('create_order/', OrderDAO.create_order, name='create_order'),
    path('create_save/', OrderDAO.order_save, name='order_save'),
    path('order_list/', OrderDAO.order_list, name='order_list'),
    path('order_detail/<id>/', OrderDAO.order_detail, name='order_detail'),
    path('order_remove/<id>/', OrderDAO.order_remove, name='order_remove'),

    # ------ PRODUCT ------
    path('', ProductDAO.render_product, name='render_product'),
    path('product/<id>/<category>/', ProductDAO.render_detail, name='render_detail'),
    path('product/<category>/', ProductDAO.render_list, name='render_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
