from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_cart_item/', views.remove_cart_item, name='remove_cart_item'),
    path('listar_pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
    # path('editar_pedido/<int:pk>/', views.editar_pedido, name='editar_pedido'),
    # path('eliminar_pedido/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('editar_pedido/', views.editar_pedido, name='editar_pedido'),
    path('editar_evidencia_pedido/', views.editar_evidencia_pedido, name='editar_evidencia_pedido'),
    path('eliminar_pedido/', views.eliminar_pedido, name='eliminar_pedido'),
    path('cambiar_estado/', views.cambiar_estado, name='cambiar_estado'),
    path('listar_mis_pedidos/', views.listar_mis_pedidos, name='listar_mis_pedidos'),

    #--------------------------------productos-----------------------------------
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('crear_productos/', views.listar_productos, name='crear_producto'),
    path('editar_productos/', views.editar_productos, name='editar_producto'),
    path('editar_evidencia_productos/', views.editar_evidencia_productos, name='editar_evidencia_productos'),
    path('cambiar_estado_productos/', views.cambiar_estado_productos, name='cambiar_estado_productos'),
    path('cambiar_estado_catalogo/', views.cambiar_estado_catalogo, name='cambiar_estado_catalogo'),
    path('eliminar_producto/', views.eliminar_producto, name='eliminar_producto'),

    #--------------------------------TIPO productos-----------------------------------

    path('listar_tipo_producto/', views.listar_tipos_productos, name='listar_tipo_producto'),
    path('editar_tipo_producto/', views.editar_tipo_producto, name='editar_tipo_producto'),
    path('eliminar_tipo_producto/', views.eliminar_tipo_producto, name='eliminar_tipo_producto'),
    path('cambiar_estado_tipo_producto/', views.cambiar_estado_tipo_producto, name='cambiar_estado_tipo_producto'),


    # -------------------------------- Tipo de Servicios --------------------------------
    path('listar_tipo_servicios/', views.listar_tipo_servicios, name='listar_tipo_servicios'),
    path('eliminar_tipo_servicio/', views.eliminar_tipo_servicios, name='eliminar_tipo_servicio'),
    path('eliminar_tipo_servicio/<int:tipoServicioId>/', views.eliminar_tipo_servicios, name='eliminar_tipo_servicio'),
    path('editar_tipo_servicio/', views.editar_tipo_servicio, name='editar_tipo_servicio'),
    path('editar_tipo_servicio/<int:tipoServicioId>/', views.editar_tipo_servicio, name='editar_tipo_servicio'),
    path('cambiar_estado_tipo_servicio/', views.cambiar_estado_tipo_servicio, name='cambiar_estado_tipo_servicio'),
    
    # -------------------------------- Servicios --------------------------------
    path('listar_servicios/', views.listar_servicios, name='listar_servicios'),
    path('editar_servicio/', views.editar_servicio, name='editar_servicio'),
    path('editar_servicio/<int:ServicioId>/', views.editar_servicio, name='editar_servicio'),
    path('eliminar_servicio/', views.eliminar_servicio, name='eliminar_servicio'),
    path('eliminar_servicio/<int:ServicioId>/', views.eliminar_servicio, name='eliminar_servicio'),
    path('editar_img_servicio/', views.editar_img_servicio, name='editar_img_servicio'),
    path('listar_servicios/', views.listar_servicios, name='listar_servicios'),
    path('cambiar_estado_servicio/', views.cambiar_estado_servicio, name='cambiar_estado_servicio'),
    path('cambiar_estado_servicio_catalogo/', views.cambiar_estado_servicio_catalogo, name='cambiar_estado_servicio_catalogo'),

    #---------------------------------Detalle productos------------------------------

    path('listar_detalle_producto/', views.listar_servicios, name='listar_servicios'),
    path('ver_carrito/', views.listar_detalle_producto, name='ver_carrito'),

    #-------------------------------ORDEN PEDIDO--------------
    path('crear-pedido-carrito/', views.crear_pedido_carrito, name='crear_pedido_carrito'),

    



    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
