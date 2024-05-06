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
]
