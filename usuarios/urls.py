from django.contrib import admin
from django.urls import path
from . import views as viewsUsuarios
app_name = 'usuarios'

urlpatterns = [
    path('hello/', viewsUsuarios.hello),
    # PERMISOS
    path('listar_permisos/', viewsUsuarios.listar_permisos, name='listar_permisos'),
    path('crear_permiso/', viewsUsuarios.crear_permiso, name='crear_permiso'),
    path('editar_permiso/<int:id_permiso>/', viewsUsuarios.editar_permiso, name='editar_permiso'),
    path('eliminar_permiso/<int:id_permiso>/', viewsUsuarios.eliminar_permiso, name='eliminar_permiso'),

    # ROLES
    path('listar_roles/', viewsUsuarios.listar_roles, name='listar_roles'),
    path('crear_rol/', viewsUsuarios.crear_rol, name='crear_rol'),
    path('editar_rol/<int:id_rol>/', viewsUsuarios.editar_rol, name='editar_rol'),
    path('eliminar_rol/<int:id_rol>/', viewsUsuarios.eliminar_rol, name='eliminar_rol'),

    # USUARIOS
    path('listar_usuarios/', viewsUsuarios.listar_usuarios, name='listar_usuarios'),
    path('crear_usuario/', viewsUsuarios.crear_usuario, name='crear_usuario'),
    path('editar_usuario/<int:id_usuario>/', viewsUsuarios.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:id_usuario>/', viewsUsuarios.eliminar_usuario, name='eliminar_usuario'),

    path('iniciar_sesion/', viewsUsuarios.iniciar_sesion, name='login'),
    path('registrarse/', viewsUsuarios.registrarse, name='register'),
    path('cerrar_sesion/', viewsUsuarios.cerrar_sesion, name='logout'),
]
