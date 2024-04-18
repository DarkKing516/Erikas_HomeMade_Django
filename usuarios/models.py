from django.db import models

class Rol(models.Model):
    nombre_rol = models.CharField(max_length=50)
    estado_rol = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.nombre_rol

class Permiso(models.Model):
    nombre_permiso = models.CharField(max_length=50)
    estado_permiso = models.CharField(max_length=1, default='A')

    def __str__(self):
        return self.nombre_permiso

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    documento = models.CharField(max_length=15)
    correo = models.EmailField()
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=255)
    estado = models.CharField(max_length=1, default='A')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class RolxPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rol} - {self.permiso}"
