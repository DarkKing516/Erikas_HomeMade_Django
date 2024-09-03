from django.core.management.base import BaseCommand
from usuarios.models import Permiso, Rol, Usuario
from tqdm import tqdm  # Importamos tqdm para la barra de progreso

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
            'Editar Estado Tipo Servicios', 'Listar Dashboard'
        ]

        # Barra de progreso para insertar permisos
        self.stdout.write('Insertando permisos...')
        permiso_objs = []
        for nombre_permiso in tqdm(permisos, desc='Progreso permisos'):
            try:
                # Eliminar permisos duplicados
                Permiso.objects.filter(nombre_permiso=nombre_permiso).delete()

                # Crear o obtener el permiso
                permiso, created = Permiso.objects.get_or_create(nombre_permiso=nombre_permiso)
                permiso_objs.append(permiso)
            except Permiso.MultipleObjectsReturned:
                self.stdout.write(self.style.ERROR(f"Multiple entries found for {nombre_permiso}, please check your data."))

        # Insertar roles
        self.stdout.write('Insertando roles...')
        rol1, created = Rol.objects.get_or_create(nombre_rol='Admin')
        rol2, created = Rol.objects.get_or_create(nombre_rol='Cliente')
        rol3, created = Rol.objects.get_or_create(nombre_rol='Testing')

        # Permisos del cliente
        permisos_cliente = [
            'Editar Perfil', 'Listar Mis Pedidos', 'Editar Mis Pedidos', 
            'Listar Mis Reservas', 'Editar Mis Reservas', 'Listar Mis Ventas'
        ]

        # Barra de progreso para asignar permisos a roles
        self.stdout.write('Asignando permisos a roles...')
        permisos_cliente_objs = Permiso.objects.filter(nombre_permiso__in=permisos_cliente)
        rol2.permisos.set(permisos_cliente_objs)

        permisos_admin = Permiso.objects.exclude(nombre_permiso__icontains='Eliminar').exclude(nombre_permiso__in=permisos_cliente)
        rol1.permisos.set(permisos_admin)
        
        rol3.permisos.set(permiso_objs)

        # Barra de progreso para insertar o actualizar usuarios
        self.stdout.write('Insertando o actualizando usuarios...')
        usuarios = [
            {'correo': 'admin@gmail.com', 'rol': rol1, 'nombre': 'Admin User', 'telefono': '1234567890', 'documento': '987654321', 'usuario': 'adminuser', 'contraseña': 'pbkdf2_sha256$720000$zMcWkNN21PjxTopxovtIhQ$sDU661j/jTud46bpOiKICosHW8IQGtCdsU/EursOcFU='},
            {'correo': 'cliente@gmail.com', 'rol': rol2, 'nombre': 'Regular User', 'telefono': '0987654321', 'documento': '123456789', 'usuario': 'regularuser', 'contraseña': 'pbkdf2_sha256$720000$zMcWkNN21PjxTopxovtIhQ$sDU661j/jTud46bpOiKICosHW8IQGtCdsU/EursOcFU='},
            {'correo': 'jhomai7020@gmail.com', 'rol': rol3, 'nombre': 'Jhon', 'telefono': '3213309427', 'documento': '1047173611', 'usuario': 'Jhon Connor', 'contraseña': 'pbkdf2_sha256$720000$zMcWkNN21PjxTopxovtIhQ$sDU661j/jTud46bpOiKICosHW8IQGtCdsU/EursOcFU='},
            {'correo': 'danilovergara257@gmail.com', 'rol': rol3, 'nombre': 'Danilo Vergara', 'telefono': '3177099118', 'documento': '104123613', 'usuario': 'Dan', 'contraseña': 'pbkdf2_sha256$720000$zMcWkNN21PjxTopxovtIhQ$sDU661j/jTud46bpOiKICosHW8IQGtCdsU/EursOcFU='},
            {'correo': 'juanfelipesanchezsanchezherrer@gmail.com', 'rol': rol3, 'nombre': 'Emmanuel Sanchez', 'telefono': '3203097136', 'documento': '1073973612', 'usuario': 'Pelos', 'contraseña': 'pbkdf2_sha256$720000$zMcWkNN21PjxTopxovtIhQ$sDU661j/jTud46bpOiKICosHW8IQGtCdsU/EursOcFU='},
            {'correo': 'valenciaalzatenelsondavid@gmail.com', 'rol': rol3, 'nombre': 'Nelson David', 'telefono': '3146060549', 'documento': '104273611', 'usuario': 'Murcia', 'contraseña': 'pbkdf2_sha256$720000$zMcWkNN21PjxTopxovtIhQ$sDU661j/jTud46bpOiKICosHW8IQGtCdsU/EursOcFU='}
        ]

        for user_data in tqdm(usuarios, desc='Progreso usuarios'):
            Usuario.objects.update_or_create(
                correo=user_data['correo'],
                defaults={
                    'idRol': user_data['rol'],
                    'nombre': user_data['nombre'],
                    'telefono': user_data['telefono'],
                    'documento': user_data['documento'],
                    'usuario': user_data['usuario'],
                    'contraseña': user_data['contraseña']
                }
            )

        self.stdout.write(self.style.SUCCESS('Datos insertados o actualizados correctamente.'))
