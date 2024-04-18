from django.contrib import admin
from django.urls import path
from . import views as viewsUsuarios

urlpatterns = [
    path('hello/', viewsUsuarios.hello),
    path('listar_roles/', viewsUsuarios.listar_roles, name='listar_roles'),
    path('crear/', viewsUsuarios.crear_rol, name='crear_rol'),
    path('editar/<int:id_rol>/', viewsUsuarios.editar_rol, name='editar_rol'),
    path('eliminar/<int:id_rol>/', viewsUsuarios.eliminar_rol, name='eliminar_rol'),
]
