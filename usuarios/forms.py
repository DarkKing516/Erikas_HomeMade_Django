from django import forms
from .models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = ['nombre_rol', 'estado_rol']
        # Puedes agregar widgets personalizados u otros atributos de campo si es necesario
