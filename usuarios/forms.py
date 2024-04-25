# from django_select2.widgets import Select2Widget
from django import forms
from .models import *

class RolForm(forms.ModelForm):
    ESTADOS_ROL = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )

    estado_rol = forms.ChoiceField(choices=ESTADOS_ROL, label='Estado')
    # permisos = forms.ModelMultipleChoiceField(queryset=Permiso.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    permisos = forms.ModelMultipleChoiceField(queryset=Permiso.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'select2'}), required=False)



    class Meta:
        model = Rol
        fields = ['nombre_rol', 'estado_rol', 'permisos']


class PermisoForm(forms.ModelForm):
    ESTADOS_PERMISO = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )

    estado_permiso = forms.ChoiceField(choices=ESTADOS_PERMISO)

    class Meta:
        model = Permiso
        fields = ['nombre_permiso', 'estado_permiso']


# class RolxPermisoForm(forms.ModelForm):
#     class Meta:
#         model = RolxPermiso
#         fields = ['idRol', 'idPermiso']  # Lista de campos que quieres incluir en el formulario

class UsuarioForm(forms.ModelForm):
    ESTADOS_USUARIO = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )

    estado = forms.ChoiceField(choices=ESTADOS_USUARIO, label='Estado')

    class Meta:
        model = Usuario
        fields = ['idRol', 'nombre', 'telefono', 'documento', 'correo', 'usuario', 'contraseña', 'estado']


class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo electrónico')
    contraseña = forms.CharField(widget=forms.PasswordInput, label='Contraseña')