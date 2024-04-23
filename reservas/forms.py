from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'fecha', 'fecha_cita', 'descripcion', 'estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'fecha_cita': forms.DateInput(attrs={'type': 'date'})
        }