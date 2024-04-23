from django import forms
from .models import Pedido, Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
    'idPedido',
    'fecha_pedido',
    'descripcion_pedido',
    'subtotal',
    'iva',
    'total',
    'evidencia_pago',
    'estado_pedido',
]
        widgets = {}

