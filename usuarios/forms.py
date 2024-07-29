# from django_select2.widgets import Select2Widget
from django import forms
from .models import *

class RolForm(forms.ModelForm):
    ESTADOS_ROL = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )

    estado_rol = forms.ChoiceField(choices=ESTADOS_ROL, label='Estado', widget=forms.Select(attrs={'class': 'form-control'}))
    nombre_rol = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))

    # permisos = forms.ModelMultipleChoiceField(queryset=Permiso.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    permisos = forms.ModelMultipleChoiceField(queryset=Permiso.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'select2 form-control js-states form-control select2-hidden-accessible', 'id': 'id_permisos'}), required=False)



    class Meta:
        model = Rol
        fields = ['nombre_rol', 'estado_rol', 'permisos']
    def clean_nombre_rol(self):
        nombre_rol = self.cleaned_data['nombre_rol']
        if self.instance.pk:  # Verifica si el rol ya existe en la base de datos
            original_rol = Rol.objects.get(pk=self.instance.pk)
            if original_rol.nombre_rol == nombre_rol:
                return nombre_rol  # El nombre del rol no ha cambiado, no es necesario validar
        if Rol.objects.filter(nombre_rol=nombre_rol).exists():
            raise forms.ValidationError("¡El nombre del rol ya existe!")
        return nombre_rol


class PermisoForm(forms.ModelForm):
    ESTADOS_PERMISO = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )

    # estado_permiso = forms.ChoiceField(choices=ESTADOS_PERMISO)
    estado_permiso = forms.ChoiceField(choices=ESTADOS_PERMISO, label='Estado', widget=forms.Select(attrs={'class': 'form-control'}))
    nombre_permiso = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    class Meta:
        model = Permiso
        fields = ['nombre_permiso', 'estado_permiso']

    def clean_nombre_permiso(self):
        nombre_permiso = self.cleaned_data['nombre_permiso']
        if self.instance.pk:  # Verifica si el permiso ya existe en la base de datos
            original_permiso = Permiso.objects.get(pk=self.instance.pk)
            if original_permiso.nombre_permiso == nombre_permiso:
                return nombre_permiso  # El nombre del permiso no ha cambiado, no es necesario validar
        if Permiso.objects.filter(nombre_permiso=nombre_permiso).exists():
            raise forms.ValidationError("¡El nombre del permiso ya existe!")
        return nombre_permiso


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
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit() or len(telefono) != 10:
            raise forms.ValidationError("El teléfono debe contener 10 dígitos y solo números.")
        return telefono

    def clean_documento(self):
        documento = self.cleaned_data['documento']
        if len(documento) < 6 or len(documento) > 15:
            raise forms.ValidationError("El documento debe tener entre 6 y 15 caracteres.")
        return documento

    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        if len(usuario) < 3 or len(usuario) > 20:
            raise forms.ValidationError("El usuario debe tener entre 3 y 20 caracteres.")
        return usuario

    def clean_contraseña(self):
        contraseña = self.cleaned_data['contraseña']
        if len(contraseña) < 4 or len(contraseña) > 100:
            raise forms.ValidationError("La contraseña debe tener entre 4 y 100 caracteres.")
        if not any(char.isdigit() for char in contraseña):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        if not any(char.isupper() for char in contraseña):
            raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not any(char.islower() for char in contraseña):
            raise forms.ValidationError("La contraseña debe contener al menos una letra minúscula.")
        # if not any(char in "!@#$%^&*()-_+=<>?{}[]|\/:;\"'`~" for char in contraseña):
        #     raise forms.ValidationError("La contraseña debe contener al menos un carácter especial.")
        return contraseña

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if Usuario.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return correo


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
        user_id = self.instance.id

        # Validar si el documento contiene solo números
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        if Usuario.objects.exclude(id=user_id).filter(documento=documento).exists():
            raise forms.ValidationError("Este documento ya está en uso.")
        return documento

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        # Validar si el teléfono contiene solo números
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono
    
    def clean_correo(self):  
        correo = self.cleaned_data['correo']  
        user_id = self.instance.id

        if Usuario.objects.exclude(id=user_id).filter(correo=correo).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return correo


class EditarUsuario(forms.ModelForm):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    telefono = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}))
    documento = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Documento'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}))
    usuario = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    idRol = forms.ModelChoiceField(queryset=Rol.objects.all(), empty_label=None, label='Rol', widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Usuario
        fields = ['idRol', 'nombre', 'telefono', 'documento', 'correo', 'usuario']
        
    def clean_documento(self):
        documento = self.cleaned_data['documento']
        user_id = self.instance.id

        # Validar si el documento contiene solo números
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")

        try:
            existing_user = Usuario.objects.exclude(id=user_id).get(documento=documento)
            if existing_user.documento == self.instance.documento:
                return documento
            else:
                raise forms.ValidationError("Este documento ya está en uso.")
        except Usuario.DoesNotExist:
            return documento

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        # Validar si el teléfono contiene solo números
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono
    def clean_correo(self):  # Aquí cambiamos 'clean_email' a 'clean_correo'
        correo = self.cleaned_data['correo']  # Aquí cambiamos 'email' a 'correo'
        user_id = self.instance.id
        try:
            existing_user = Usuario.objects.exclude(id=user_id).get(correo=correo)  # Aquí cambiamos 'User' a 'Usuario' y 'email' a 'correo'
            # Si el correo electrónico ya está en uso pero es el mismo que el actual,
            # entonces no hay conflicto y podemos permitir que pase la validación.
            if existing_user.correo == self.instance.correo:
                return correo
            else:
                raise forms.ValidationError("Este correo electrónico ya está en uso.")
        except Usuario.DoesNotExist:  # Aquí cambiamos 'User' a 'Usuario'
            return correo

class EditarContraseñaUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['contraseña']
        
class ForgotForm(forms.Form):
    correo = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={'class': 'inputField', 'id': 'email', 'placeholder': 'Email'}))
