from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'fecha_cita', 'descripcion']
        widgets = {
            # 'fecha': forms.DateInput(attrs={'type': 'date'}),
            'fecha_cita': forms.DateTimeInput(attrs={'type': 'datetime-local'})  # Usa DateTimeInput para fechas y horas
            # 'descripcion': forms.Textarea(attrs={'type': 'textarea'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['fecha'].widget = forms.HiddenInput()
            # Opcionalmente, si deseas mostrar la fecha de reserva pero sin ser editable:
            # self.fields['fecha'].widget.attrs['readonly'] = True

class ReservaFormEditar(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'fecha', 'fecha_cita', 'descripcion', 'estado']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_cita': forms.DateTimeInput(attrs={'type': 'datetime-local'})
            # 'descripcion': forms.Textarea(attrs={'type': 'textarea'})

        }