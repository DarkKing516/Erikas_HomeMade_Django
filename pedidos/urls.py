from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('listar_pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
    # path('editar_pedido/<int:pk>/', views.editar_pedido, name='editar_pedido'),
    # path('eliminar_pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('editar_pedido/', views.editar_pedido, name='editar_pedido'),
    path('editar_evidencia_pedido/', views.editar_evidencia_pedido, name='editar_evidencia_pedido'),
    path('eliminar_pedido/', views.eliminar_pedido, name='eliminar_pedido'),
    path('cambiar_estado/', views.cambiar_estado, name='cambiar_estado'),

    #--------------------------------productos-----------------------------------
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('crear_productos/', views.listar_productos, name='crear_producto'),
    path('editar_productos/', views.editar_productos, name='editar_producto'),
    path('editar_evidencia_productos/', views.editar_evidencia_productos, name='editar_evidencia_productos'),
    path('cambiar_estado/', views.cambiar_estado, name='cambiar_estado'),

    #--------------------------------TIPO productos-----------------------------------

    path('listar_tipo_producto/', views.listar_tipos_productos, name='listar_tipo_producto'),
    path('editar_tipo_producto/', views.editar_tipo_producto, name='editar_tipo_producto'),
    path('eliminar_tipo_producto/', views.eliminar_tipo_producto, name='eliminar_tipo_producto'),

    # -------------------------------- Tipo de Servicios --------------------------------
    path('listar_tipo_servicios/', views.listar_tipo_servicios, name='listar_tipo_servicios'),
    path('eliminar_tipo_servicios/', views.eliminar_tipo_servicios, name='eliminar_tipo_servicios'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
