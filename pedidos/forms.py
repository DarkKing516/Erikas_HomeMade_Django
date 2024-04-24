from django import forms
from .models import Pedido, Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['id_Usuario','idPedido', 'fecha_pedido', 'descripcion_pedido', 'subtotal', 'iva', 'total','estado_pedido']
        widgets = {
            'fecha_pedido': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'descripcion_pedido': forms.Textarea(attrs={'type': 'textarea'}),
        }

