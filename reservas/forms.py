from django import forms
from .models import Reserva
from django.utils import timezone
from datetime import datetime

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'fecha_cita', 'descripcion']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'fecha_cita': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
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
            'fecha_cita': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input', 'placeholder': 'Fecha'}),
            'usuario': forms.Select(attrs={'class': 'form-input', 'placeholder': 'Usuario'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-input textarea-lg', 'placeholder': 'Descripción'}),
        }

    def clean_fecha_cita(self):
        fecha_cita = self.cleaned_data.get('fecha_cita')
        if fecha_cita:
            hora_inicio = datetime.time(7, 0)
            hora_fin = datetime.time(20, 0)
            if not (hora_inicio <= fecha_cita.time() <= hora_fin):
                raise forms.ValidationError("La hora debe estar entre las 7:00 AM y las 8:00 PM.")
        return fecha_cita


class ReservaFormEditar(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_cita', 'descripcion', 'estado']
        widgets = {
            'estado': forms.Select(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Completada', 'Completada')])
        }


        def clean_fecha_cita(self):
            fecha_cita = self.cleaned_data.get('fecha_cita')
            if fecha_cita < datetime.now().date():
                raise forms.ValidationError("La fecha de la cita no puede ser anterior a la fecha actual.")
            elif fecha_cita < self.instance.fecha.date():
                raise forms.ValidationError("La fecha de la cita no puede ser anterior a la fecha de la reserva actual.")
            return fecha_cita

        

        