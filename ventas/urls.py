from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .views import VentaViewSet

router = DefaultRouter()
router.register(r'ventasAPI', VentaViewSet)

app_name = 'ventas'

urlpatterns = [
    path('', include(router.urls)),
    path('listar_ventas/', views.listar_ventas, name='listar_ventas'),
    path('listar_mis_ventas/', views.listar_mis_ventas, name='listar_mis_ventas'),
    path('crear_venta/', views.crear_venta, name='crear_venta'),
    path('obtener-total-pedido/<int:idPedido>/', views.obtener_total_pedido, name='obtener_total_pedido'),
    path('obtener-pedidos-usuario/<int:usuario_id>/', views.obtener_pedidos_usuario, name='obtener_pedidos_usuario'),
    path('factura/<int:venta_id>/', views.generate_invoice, name='generate_invoice'),

]
