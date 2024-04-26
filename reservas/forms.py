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

        
class ReservaFormIndex(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'fecha_cita', 'descripcion']
        widgets = {
            # 'fecha': forms.DateInput(attrs={'type': 'date'}),
            'fecha_cita': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Usa DateTimeInput para fechas y horas
            # 'descripcion': forms.Textarea(attrs={'type': 'textarea'})
            'usuario': forms.Select(attrs={'class': 'form-input', 'placeholder': 'Usuario'}),  # Agrega la clase 'form-input'
            'fecha_cita': forms.DateTimeInput(attrs={'class': 'form-input', 'placeholder': 'Fecha', 'type': 'datetime-local'}),  # Agrega la clase 'form-input'
            'descripcion': forms.Textarea(attrs={'class': 'form-input textarea-lg', 'placeholder': 'Descripción'}),  # Agrega las clases 'form-input' y 'textarea-lg'

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
            'fecha': forms.DateTimeInput(attrs={'readonly': 'readonly'}),
            # 'usuario': forms.TextInput(attrs={'readonly': 'readonly'}),
             'estado': forms.Select(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completada', 'Completada')])
        }

        