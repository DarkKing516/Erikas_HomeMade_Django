# usuarios/serializers.py
from rest_framework import serializers
from .models import Usuario, Rol, Permiso

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    permisos = PermisoSerializer(many=True, read_only=True)

    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    idRol = RolSerializer(read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'