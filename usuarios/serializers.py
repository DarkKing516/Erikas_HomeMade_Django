# usuarios/serializers.py
from rest_framework import serializers
from .models import Usuario, Rol, Permiso
from django.contrib.auth.hashers import make_password


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
        extra_kwargs = {'contraseña': {'write_only': True}}

    def create(self, validated_data):
        validated_data['contraseña'] = make_password(validated_data.get('contraseña'))
        return super(UsuarioSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if 'contraseña' in validated_data and validated_data['contraseña']:
            validated_data['contraseña'] = make_password(validated_data['contraseña'])
        else:
            # Keep the existing password if new password is not provided
            validated_data.pop('contraseña', None)
        return super(UsuarioSerializer, self).update(instance, validated_data)