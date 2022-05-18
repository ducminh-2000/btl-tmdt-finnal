from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_product, name='render_product'),
    path('product/<id>/<category>/', views.render_detail, name='render_detail'),
    path('product/<category>/', views.render_list, name='render_list'),

]