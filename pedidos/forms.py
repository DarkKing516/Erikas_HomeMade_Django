from django import forms
from .models import Pedido
from usuarios.models import Usuario
from datetime import datetime




class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['id_Usuario', 'fecha_pedido', 'descripcion_pedido', 'subtotal', 'iva', 'total', 'estado_pedido', 'evidencia_pago']
        widgets = {
            'fecha_pedido': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'descripcion_pedido': forms.Textarea(attrs={'type': 'textarea'}),
            'evidencia_pago': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }


class CreatePedidoForm(forms.ModelForm):
    id_Usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), label='Usuario', widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_pedido = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de Pedido', 'type': 'datetime-local'}))
    descripcion_pedido = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del Pedido'}))
    subtotal = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Subtotal'}))
    iva = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'IVA'}))
    total = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total'}))
    evidencia_pago = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    estado_pedido = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado del Pedido'}))

    class Meta:
        model = Pedido
        fields = ['id_Usuario', 'fecha_pedido', 'descripcion_pedido', 'subtotal', 'iva', 'total', 'evidencia_pago', 'estado_pedido']


class PedidoFormEditarEvidencia(forms.ModelForm):
    evidencia_pago = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Pedido
        fields = [ 'evidencia_pago']
        
        
        
class PedidoFormEditar(forms.ModelForm):    
    class Meta:
        model = Pedido
        fields = ['fecha_pedido', 'descripcion_pedido', 'subtotal', 'iva', 'total']



        def clean_fecha_pedido(self):
            fecha_pedido = self.cleaned_data.get('fecha_pedido')
            if fecha_pedido < datetime.now().date():
                raise forms.ValidationError("La fecha del pedido no puede ser anterior a la fecha actual.")
            elif fecha_pedido < self.instance.fecha.date():
                raise forms.ValidationError("La fecha del pedido no puede ser anterior a la fecha del pedido actual.")
            return fecha_pedido
        
