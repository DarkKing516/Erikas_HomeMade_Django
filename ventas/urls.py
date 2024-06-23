from django.contrib import admin
from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('listar_ventas/', views.listar_ventas, name='listar_ventas'),
    path('listar_mis_ventas/', views.listar_mis_ventas, name='listar_mis_ventas'),
    path('crear_venta/', views.crear_venta, name='crear_venta'),
    path('obtener-total-pedido/<int:idPedido>/', views.obtener_total_pedido, name='obtener_total_pedido'),
    path('obtener-pedidos-usuario/<int:usuario_id>/', views.obtener_pedidos_usuario, name='obtener_pedidos_usuario'),
    path('generar_factura/<int:idVenta>/', views.generar_factura_pdf, name='generar_factura'),

]
