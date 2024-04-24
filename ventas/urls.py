from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('listar_ventas/', views.listar_ventas, name='listar_ventas'),
    path('crear_venta/', views.crear_venta, name='crear_venta'),
]
