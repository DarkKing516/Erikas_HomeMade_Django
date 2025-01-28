# usuarios/models.py
from django.contrib.auth.hashers import make_password, check_password
from django.db import models

class Permission(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'permisos'  # Personalizando el nombre de la tabla

class Role(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'roles'  # Personalizando el nombre de la tabla

class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.SET_DEFAULT, default=2)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    id_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='user_images/', default='user_images/iconosesion.jpg')  # Campo de imagen con valor predeterminado

    def set_password(self, password):
        """Utiliza el método de Django para establecer la contraseña hasheada"""
        self.password = make_password(password)

    def check_password(self, password):
        """Verifica si la contraseña proporcionada coincide con la almacenada"""
        return check_password(password, self.password)
    def __str__(self):
        return f"{self.name} - {self.id_number}"
    class Meta:
        db_table = 'usuarios'  # Personalizando el nombre de la tabla


# class RolxPermiso(models.Model):
#     idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
#     idPermiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.idRol.nombre_rol} - {self.idPermiso.nombre_permiso}"
#     class Meta:
#         db_table = 'rolxpermiso'  # Personalizando el nombre de la tabla
