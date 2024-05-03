from django.contrib import admin
from django.urls import path
from . import views as viewsPedidos
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('listar_pedidos/', viewsPedidos.listar_pedidos, name='listar_pedidos'),
    path('crear_pedido/', viewsPedidos.crear_pedido, name='crear_pedido'),
    path('editar_pedido/<int:pk>/', views.editar_pedido, name='editar_pedido'),
    path('eliminar_pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('eliminar_pedido/', views.eliminar_pedido, name='eliminar_pedido'),
    path('cambiar_estado/', views.cambiar_estado, name='cambiar_estado'),
]