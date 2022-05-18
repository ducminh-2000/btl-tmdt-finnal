from django.urls import path

from . import views

urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
    path('create_save/', views.order_save, name='order_save'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/<id>/', views.order_detail, name='order_detail'),
    path('order_remove/<id>/', views.order_remove, name='order_remove'),
]