# usuarios/backends.py
from django.contrib.auth.backends import BaseBackend
from .models import Usuario

class CustomBackend(BaseBackend):
    def authenticate(self, request, correo=None, contraseña=None):
        try:
            usuario = Usuario.objects.get(correo=correo)
            if usuario.verificar_contraseña(contraseña):
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
