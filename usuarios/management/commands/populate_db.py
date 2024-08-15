from django.core.management.base import BaseCommand
from usuarios.models import Permiso, Rol, Usuario

class Command(BaseCommand):
    help = 'Popula la base de datos con permisos, roles y usuarios'

    def handle(self, *args, **kwargs):
        # Insertar permisos
        permisos = [
            'Listar Usuarios', 'Crear Usuarios', 'Editar Usuarios', 'Editar Rol Usuarios', 
            'Editar Estado Usuarios', 'Editar Perfil', 'Eliminar Usuarios', 'Listar Roles', 
            'Crear Roles', 'Editar Roles', 'Editar Estado Roles', 'Eliminar Roles', 
            'Listar Permisos', 'Editar Permisos', 'Editar Estado Permisos', 'Listar Productos', 
            'Crear Productos', 'Editar Productos', 'Eliminar Productos', 'Listar Tipo Productos', 
            'Crear Tipo Productos', 'Editar Tipo Productos', 'Eliminar Tipo Productos', 
            'Listar Servicios', 'Crear Servicios', 'Editar Servicios', 'Eliminar Servicios', 
            'Listar Tipo Servicios', 'Crear Tipo Servicios', 'Editar Tipo Servicios', 
            'Eliminar Tipo Servicios', 'Listar Pedidos', 'Listar Mis Pedidos', 'Crear Pedidos', 
            'Editar Pedidos', 'Editar Mis Pedidos', 'Eliminar Pedidos', 'Listar Reservas', 
            'Listar Mis Reservas', 'Crear Reservas', 'Editar Reservas', 'Editar Mis Reservas', 
            'Eliminar Reservas', 'Listar Ventas', 'Crear Ventas', 'Listar Mis Ventas', 
            'Crear Permisos', 'Eliminar Permisos', 'Editar Estado Pedidos', 
            'Editar Evidencia Pedidos', 'Editar Estado Tipo Productos', 'Editar Estado Productos', 
            'Editar Estado Catalogo Productos', 'Cambiar Imagen Productos', 
            'Cambiar Imagen Servicios', 'Editar Estado Servicio Catalogo', 'Editar Estado Servicio', 
            'Editar Estado Tipo Servicios'
        ]

        permiso_objs = []
        for nombre_permiso in permisos:
            try:
                # Eliminar permisos duplicados
                Permiso.objects.filter(nombre_permiso=nombre_permiso).delete()

                # Crear o obtener el permiso
                permiso, created = Permiso.objects.get_or_create(nombre_permiso=nombre_permiso)
                permiso_objs.append(permiso)
            except Permiso.MultipleObjectsReturned:
                self.stdout.write(self.style.ERROR(f"Multiple entries found for {nombre_permiso}, please check your data."))

        # Insertar roles
        rol1, created = Rol.objects.get_or_create(nombre_rol='Admin')
        rol2, created = Rol.objects.get_or_create(nombre_rol='Cliente')

        # Asignar permisos a roles
        rol1.permisos.set(permiso_objs)
        
        # Insertar o actualizar usuarios
        usuario1, created = Usuario.objects.update_or_create(
            correo='jhomai7020@gmail.com',
            defaults={
                'idRol': rol1,
                'nombre': 'Admin User',
                'telefono': '1234567890',
                'documento': '987654321',
                'usuario': 'adminuser',
                'contraseña': '1234'
            }
        )

        usuario2, created = Usuario.objects.update_or_create(
            correo='use1r@gmail.com',
            defaults={
                'idRol': rol2,
                'nombre': 'Regular User',
                'telefono': '0987654321',
                'documento': '123456789',
                'usuario': 'regularuser',
                'contraseña': 'userpassword'
            }
        )

        self.stdout.write(self.style.SUCCESS('Datos insertados o actualizados correctamente.'))
