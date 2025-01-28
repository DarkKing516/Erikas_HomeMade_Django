from django.core.management.base import BaseCommand
from usuarios.models import *
from tqdm import tqdm  # Importamos tqdm para la barra de progreso

class Command(BaseCommand):
    help = 'Popula la base de datos con permisos, roles y usuarios'

    def handle(self, *args, **kwargs):
        # Insertar permisos
        permissions = [
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

        self.stdout.write('Insertando permisos...')
        permission_objs = []
        for permission_name in tqdm(permissions, desc='Progreso permisos'):
            permission, created = Permission.objects.get_or_create(name=permission_name)
            permission_objs.append(permission)

        # Insertar roles
        self.stdout.write('Insertando roles...')
        role_admin, _ = Role.objects.get_or_create(name='Admin')
        role_client, _ = Role.objects.get_or_create(name='Cliente')
        role_testing, _ = Role.objects.get_or_create(name='Testing')

        # Permisos del cliente
        client_permissions = [
            'Editar Perfil', 'Listar Mis Pedidos', 'Editar Mis Pedidos', 
            'Listar Mis Reservas', 'Editar Mis Reservas', 'Listar Mis Ventas'
        ]

        self.stdout.write('Asignando permisos a roles...')
        client_permission_objs = Permission.objects.filter(name__in=client_permissions)
        role_client.permissions.set(client_permission_objs)

        admin_permissions = Permission.objects.exclude(name__icontains='Eliminar').exclude(name__in=client_permissions)
        role_admin.permissions.set(admin_permissions)

        role_testing.permissions.set(permission_objs)

        # Insertar usuarios
        self.stdout.write('Insertando o actualizando usuarios...')
        users = [
            {'email': 'admin@gmail.com', 'role': role_admin, 'name': 'Admin User', 'phone': '1234567890', 'id_number': '987654321', 'username': 'adminuser', 'password': '1234'},
            {'email': 'cliente@gmail.com', 'role': role_client, 'name': 'Regular User', 'phone': '0987654321', 'id_number': '123456789', 'username': 'regularuser', 'password': '1234'},
            {'email': 'jhomai7020@gmail.com', 'role': role_testing, 'name': 'Jhon', 'phone': '3213309427', 'id_number': '1047173611', 'username': 'JhonConnor', 'password': '1234'},
            {'email': 'danilovergara257@gmail.com', 'role': role_testing, 'name': 'Danilo Vergara', 'phone': '3177099118', 'id_number': '104123613', 'username': 'Dan', 'password': '1234'},
            {'email': 'juanfelipesanchezsanchezherrer@gmail.com', 'role': role_testing, 'name': 'Emmanuel Sanchez', 'phone': '3203097136', 'id_number': '1073973612', 'username': 'Pelos', 'password': '1234'},
            {'email': 'valenciaalzatenelsondavid@gmail.com', 'role': role_testing, 'name': 'Nelson David', 'phone': '3146060549', 'id_number': '104273611', 'username': 'Murcia', 'password': '1234'}
        ]

        for user_data in tqdm(users, desc='Progreso usuarios'):
            user, created = User.objects.update_or_create(
                email=user_data['email'],
                defaults={
                    'role': user_data['role'],
                    'name': user_data['name'],
                    'phone': user_data['phone'],
                    'id_number': user_data['id_number'],
                    'username': user_data['username'],
                    'active': True
                }
            )
            if created or not user.check_password(user_data['password']):
                user.set_password(user_data['password'])
                user.save()

        self.stdout.write(self.style.SUCCESS('Datos insertados o actualizados correctamente.'))
