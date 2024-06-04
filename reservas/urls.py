from django.contrib import admin
from django.urls import path
from . import views as viewsReservas
app_name = 'reservas'

urlpatterns = [
    path('hello/', viewsReservas.hello),
    path('listar_reservas/', viewsReservas.listar_reservas, name='listar_reserva'),
    path('crear_reserva/', viewsReservas.crear_reserva, name='crear_reserva'),
    # path('editar/<int:id_reserva>/', viewsReservas.editar_reserva, name='editar_reserva'),
    path('editar/', viewsReservas.editar_reserva, name='editar_reserva'),
    # path('eliminar/<int:id_reserva>/', viewsReservas.eliminar_reserva, name='eliminar_reserva'),
    path('eliminar/', viewsReservas.eliminar_reserva, name='eliminar_reserva'),
    path('listar_reservas_cliente/', viewsReservas.listar_reservas_cliente, name='listar_reserva_cliente'),
    path('cambiar_estado_reserva/', viewsReservas.cambiar_estado_reserva, name='cambiar_estado_reserva'),
    path('cambiar_fecha_reserva/', viewsReservas.cambiar_fecha_reserva, name='cambiar_fecha_reserva'),

]
