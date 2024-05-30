from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views as viewsUsuarios
app_name = 'usuarios'

urlpatterns = [
    path('hello/', viewsUsuarios.hello),
    # PERMISOS
    path('listar_permisos/', viewsUsuarios.listar_permisos, name='listar_permisos'),
    path('crear_permiso/', viewsUsuarios.crear_permiso, name='crear_permiso'),
    path('editar_permiso/<int:id_permiso>/', viewsUsuarios.editar_permiso, name='editar_permiso'),
    path('editar_permiso/', viewsUsuarios.editar_permiso, name='editar_permiso'),
    path('cambiar_estado_permiso/', viewsUsuarios.cambiar_estado_permiso, name='cambiar_estado_permiso'),
    path('eliminar_permiso/<int:id_permiso>/', viewsUsuarios.eliminar_permiso, name='eliminar_permiso'),

    # ROLES
    path('listar_roles/', viewsUsuarios.listar_roles, name='listar_roles'),
    path('crear_rol/', viewsUsuarios.crear_rol, name='crear_rol'),
    path('editar_rol/<int:id_rol>/', viewsUsuarios.editar_rol, name='editar_rol'),
    path('editar_rol/', viewsUsuarios.editar_rol, name='editar_rol'),
    path('cambiar_estado_rol/', viewsUsuarios.cambiar_estado_rol, name='cambiar_estado_rol'),
    path('eliminar_rol/<int:id_rol>/', viewsUsuarios.eliminar_rol, name='eliminar_rol'),
    # path('eliminar_rol/', viewsUsuarios.eliminar_rol, name='eliminar_rol'),

    # USUARIOS
    path('listar_usuarios/', viewsUsuarios.listar_usuarios, name='listar_usuarios'),
    path('crear_usuario/', viewsUsuarios.crear_usuario, name='crear_usuario'),
    path('cambiar_rol/', viewsUsuarios.cambiar_rol, name='cambiar_rol'),
    path('cambiar_estado/', viewsUsuarios.cambiar_estado, name='cambiar_estado'),
    path('editar_usuario/', viewsUsuarios.editar_usuario, name='editar_usuario'),
    path('editar_usuario_/<int:id_usuario>/', viewsUsuarios.editar_usuario_, name='editar_usuario_'),
    path('eliminar_usuario/', viewsUsuarios.eliminar_usuario, name='eliminar_usuario'),
    path('eliminar_usuario/<int:id_usuario>/', viewsUsuarios.eliminar_usuario, name='eliminar_usuario'),

    path('iniciar_sesion/', viewsUsuarios.iniciar_sesion, name='login'),
    path('registrarse/', viewsUsuarios.registrarse, name='register'),
    path('editar_perfil/', viewsUsuarios.editar_account, name='editar_account'),
    path('editar_contraseña/', viewsUsuarios.editar_contraseña, name='editar_contraseña'),
    path('cerrar_sesion/', viewsUsuarios.cerrar_sesion, name='logout'),
    path('requestLogin/', viewsUsuarios.requestLogin, name='requestLogin'),
    path('recuperar Contraseña/', viewsUsuarios.forgotPassword, name='forgotPassword'),
    path('editar_foto_perfil/', viewsUsuarios.editar_foto_perfil, name='editar_foto_perfil'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)