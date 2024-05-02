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

    estado = forms.ChoiceField(choices=ESTADOS_USUARIO, label='Estado', widget=forms.Select(attrs={'class': 'form-control'}))
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    telefono = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}))
    documento = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}))
    usuario = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    contraseña = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    idRol = forms.ModelChoiceField(queryset=Rol.objects.all(), empty_label=None, label='Rol', widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Usuario
        fields = ['idRol', 'nombre', 'telefono', 'documento', 'correo', 'usuario', 'contraseña', 'estado']


class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class': 'inputField', 'id': 'email', 'placeholder': 'Email'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'inputField', 'id': 'password', 'placeholder': 'Contraseña'}), label='Contraseña')




class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'telefono', 'documento', 'correo', 'usuario', 'contraseña']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'inputField', 'placeholder': 'Nombre'}),
            'telefono': forms.TextInput(attrs={'class': 'inputField', 'placeholder': 'Teléfono'}),
            'documento': forms.TextInput(attrs={'class': 'inputField', 'placeholder': 'Documento'}),
            'correo': forms.EmailInput(attrs={'class': 'inputField', 'placeholder': 'Correo'}),
            'usuario': forms.TextInput(attrs={'class': 'inputField', 'placeholder': 'Usuario'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'inputField', 'placeholder': 'Contraseña'}),
        }
    def clean_documento(self):
        documento = self.cleaned_data['documento']
        # Validar si el documento contiene solo números
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        # Validar si el teléfono contiene solo números
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono


class CreateUsuario(forms.ModelForm):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    telefono = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}))
    documento = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}))
    usuario = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    contraseña = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    idRol = forms.ModelChoiceField(queryset=Rol.objects.all(), empty_label=None, label='Rol', widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Usuario
        fields = ['idRol', 'nombre', 'telefono', 'documento', 'correo', 'usuario', 'contraseña']
        
    def clean_documento(self):
        documento = self.cleaned_data['documento']
        # Validar si el documento contiene solo números
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        # Validar si el teléfono contiene solo números
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono