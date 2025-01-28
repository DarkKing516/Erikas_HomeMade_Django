# usuarios/serializers.py
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    permisos = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # idRol = RoleSerializer(read_only=True)
    id_number = serializers.CharField(max_length=15, label="N° Documento")
    profile_image = serializers.ImageField(read_only=True)
    password = serializers.CharField( required=False)

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ['profile_image']  # Excluye el campo 'profile_image'
        # fields = ['id', 'role', 'name', 'phone', 'id_number', 'email', 'username', 'active']

    def create(self, validated_data):
        """Hashea la contraseña antes de guardar el usuario"""
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)  # Hasheamos la contraseña
        user.save()
        return user

    def update(self, instance, validated_data):
        """Hashea la nueva contraseña si es proporcionada"""
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)  # Hasheamos la contraseña
        instance.save()
        return instance
