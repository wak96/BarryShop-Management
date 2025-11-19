from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('settings/', views.settings, name='settings'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
    path('inventory/', views.inventory, name='inventory'),
    path('customers', views.customers, name='customer'),
    path('categories/', views.categories, name='categories'),
    path('barcode/', views.barcode, name='barcode'),
]