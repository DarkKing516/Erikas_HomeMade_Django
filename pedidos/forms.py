from django import forms
from .models import *
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
        
#------------------------------------------------------------productos---------------------------------------------------------

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'id_TipoProducto', 'nombre', 'descripcion', 'imagen', 'precio', 'estado_producto', 'estado_catalogo', 'cantidad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'type': 'textarea'}),
            'imagen': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)


class CreateProductoForm(forms.ModelForm):
    id_TipoProducto = forms.ModelChoiceField(queryset=TipoProducto.objects.all(), label='Tipo de Producto', widget=forms.Select(attrs={'class': 'form-control'}))
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    descripcion = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}))
    estado_producto = forms.CharField(max_length=1, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado del Producto'}))
    estado_catalogo = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}))

    class Meta:
        model = Producto
        fields = ['id_TipoProducto', 'nombre', 'descripcion', 'imagen', 'precio', 'estado_producto', 'estado_catalogo', 'cantidad']

class editProductoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    descripcion = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}))
    estado_producto = forms.CharField(max_length=1, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado del Producto'}))
    estado_catalogo = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}))

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'estado_producto', 'estado_catalogo', 'cantidad']