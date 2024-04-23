from django.contrib import admin
from django.urls import path
from . import views as viewsPedidos
app_name = 'pedidos'

urlpatterns = [
    path('listar_pedidos/', viewsPedidos.listar_pedidos, name='listar_pedidos'),
    path('crear_pedido/', viewsPedidos.crear_pedido, name='crear_pedido'),
]