from django.contrib.auth.hashers import check_password
from django.db import models

class Permiso(models.Model):
    nombre_permiso = models.CharField(max_length=50)
    estado_permiso = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.nombre_permiso
    class Meta:
        db_table = 'permisos'  # Personalizando el nombre de la tabla

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    estado_rol = models.CharField(max_length=1, default='A')
    permisos = models.ManyToManyField(Permiso)

    def __str__(self):
        return self.nombre_rol
    class Meta:
        db_table = 'roles'  # Personalizando el nombre de la tabla

class Usuario(models.Model):
    idRol = models.ForeignKey(Rol, on_delete=models.SET_DEFAULT, default=2)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    documento = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50, unique=True)
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=255)
    estado = models.CharField(max_length=1, default='A')
    imagen = models.ImageField(upload_to='user_images/', default='user_images/iconosesion.jpg')  # Campo de imagen con valor predeterminado

    def verificar_contraseña(self, contraseña):
        return check_password(contraseña, self.contraseña)
    def __str__(self):
        return f"{self.nombre} - {self.documento}"
    class Meta:
        db_table = 'usuarios'  # Personalizando el nombre de la tabla


# class RolxPermiso(models.Model):
#     idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
#     idPermiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.idRol.nombre_rol} - {self.idPermiso.nombre_permiso}"
#     class Meta:
#         db_table = 'rolxpermiso'  # Personalizando el nombre de la tabla
