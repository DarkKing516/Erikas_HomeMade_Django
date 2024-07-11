from django import forms
from .models import *
from usuarios.models import *
from django.utils import timezone
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
    subtotal = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Subtotal', 'readonly': True})
    )
    iva = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'IVA', 'readonly': True})
    )
    total = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total', 'readonly': True})
    )
    evidencia_pago = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    estado_pedido = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado del Pedido'}))

    class Meta:
        model = Pedido
        fields = ['id_Usuario', 'fecha_pedido', 'descripcion_pedido', 'subtotal', 'iva', 'total', 'evidencia_pago', 'estado_pedido']
        widgets = {
            'fecha_pedido': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Usa DateTimeInput para fechas y horas
            'fecha_pedido': forms.DateTimeInput(attrs={'class': 'form-input', 'placeholder': 'Fecha', 'type': 'datetime-local'})
        }
        
    def clean_fecha_pedido(self):
        fecha_pedido = self.cleaned_data.get('fecha_pedido')
        if fecha_pedido and fecha_pedido.date() < datetime.now().date():
            raise forms.ValidationError("La fecha del pedido no puede ser anterior a la fecha actual.")
        return fecha_pedido


class PedidoFormEditarEvidencia(forms.ModelForm):
    evidencia_pago = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Pedido
        fields = ['evidencia_pago']

    def clean(self):
        cleaned_data = super().clean()
        pedido = self.instance

        # Verificar si el estado del pedido es "Por hacer"
        if pedido.estado_pedido != 'Por hacer':
            raise forms.ValidationError("No se puede cambiar la evidencia de pago si el estado del pedido no es 'Por hacer'.")

        return cleaned_data

        
        
        
class PedidoFormEditar(forms.ModelForm):    
    class Meta:
        model = Pedido
        fields = ['descripcion_pedido']

        
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
    id_TipoProducto = forms.ModelChoiceField(queryset=TipoProducto.objects.filter(estado_producto='Activo'), label='Tipo de Producto', widget=forms.Select(attrs={'class': 'form-control'}))
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    descripcion = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}))
    estado_producto = forms.CharField(max_length=1, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado del Producto'}))
    estado_catalogo = forms.CharField(max_length=1, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado del Catalogo'}))
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}))

    class Meta:
        model = Producto
        fields = ['id_TipoProducto', 'nombre', 'descripcion', 'imagen', 'precio', 'estado_producto', 'estado_catalogo', 'cantidad']

        
class ProductoFormEditar(forms.ModelForm):  
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
  
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'estado_producto', 'estado_catalogo', 'cantidad']        

class ProductoFormEditarEvidencia(forms.ModelForm):
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Producto
        fields = ['imagen']

        
#------------------------------------------------------------TIPO productos---------------------------------------------------------
        
        
        
class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['nombre_producto', 'estado_producto']

    def __init__(self, *args, **kwargs):
        super(TipoProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombre_producto'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado_producto'].widget.attrs.update({'class': 'form-control'})


class TipoProductoFormEditar(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['nombre_producto', 'estado_producto']
        
        
        
# ---------------- Tipo Servicios ----------------
class TipoServicioForm(forms.ModelForm):
    ESTADOS_TIPO_SERVICIO = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    estado_tipoServicio = forms.ChoiceField(choices=ESTADOS_TIPO_SERVICIO, label='Estado', widget=forms.Select(attrs={'class': 'form-control'}))
    nombre_tipoServicio = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))

    class Meta:
        model = TipoServicio
        fields = ['nombre_tipoServicio', 'estado_tipoServicio']

    def clean_nombre_tipoServicio(self):
        nombre_tipoServicio = self.cleaned_data['nombre_tipoServicio']
        if self.instance.pk:  # Verifica si el tipo de servicio ya existe en la base de datos
            original_tipo_servicio = TipoServicio.objects.get(pk=self.instance.pk)
            if original_tipo_servicio.nombre_tipoServicio == nombre_tipoServicio:
                return nombre_tipoServicio  # El nombre del tipo de servicio no ha cambiado, no es necesario validar
        if TipoServicio.objects.filter(nombre_tipoServicio=nombre_tipoServicio).exists():
            raise forms.ValidationError("¡El nombre del tipo de servicio ya existe!")
        return nombre_tipoServicio
    
    # ---------------- Servicios ----------------

class ServicioForm(forms.ModelForm):
    
    nombre_servicio = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Servicio'}))
    id_TipoServicio = forms.ModelChoiceField(queryset=TipoServicio.objects.all(), empty_label=None, label='Tipo Servicio', widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}))
    precio_servicio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}))
    img = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Servicio
        fields = ['id_TipoServicio', 'nombre_servicio', 'descripcion', 'precio_servicio', 'img']

    def clean_nombre_servicio(self):
        nombre_servicio = self.cleaned_data['nombre_servicio']
        if self.instance.pk:  # Verifica si el servicio ya existe en la base de datos
            original_servicio = Servicio.objects.get(pk=self.instance.pk)
            if original_servicio.nombre_servicio == nombre_servicio:
                return nombre_servicio  # El nombre del servicio no ha cambiado, no es necesario validar
        if Servicio.objects.filter(nombre_servicio=nombre_servicio).exists():
            raise forms.ValidationError("¡El nombre del servicio ya existe!")
        return nombre_servicio
    
class EditarServicioForm(forms.ModelForm):
    nombre_servicio = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Servicio'}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 3}))
    precio_servicio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}))

    class Meta:
        model = Servicio
        fields = ['id_TipoServicio', 'nombre_servicio', 'descripcion', 'precio_servicio']

    def clean_nombre_servicio(self):
        nombre_servicio = self.cleaned_data['nombre_servicio']
        if self.instance.pk:  # Verifica si el servicio ya existe en la base de datos
            original_servicio = Servicio.objects.get(pk=self.instance.pk)
            if original_servicio.nombre_servicio == nombre_servicio:
                return nombre_servicio  # El nombre del servicio no ha cambiado, no es necesario validar
        if Servicio.objects.filter(nombre_servicio=nombre_servicio).exists():
            raise forms.ValidationError("¡El nombre del servicio ya existe!")
        return nombre_servicio
    
class ServicioFormEditarImg(forms.ModelForm):
    img = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Servicio
        fields = ['img']
        
        
        
# --------------------------- Detalles ---------------------------
        
class DetallePedidoProductoForm(forms.ModelForm):
    idProducto = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'select2 form-control js-states form-control select2-hidden-accessible', 'id': 'idProducto'}), required=False)
    class Meta:
        model = DetallePedidoProducto
        fields = ['idProducto', 'cant_productos', 'nombre_productos', 'descripcion', 'precio_inicial_producto', 'subtotal_productos']

class DetallePedidoServicioForm(forms.ModelForm):
    idServicio = forms.ModelMultipleChoiceField(queryset=Servicio.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'select2 form-control js-states form-control select2-hidden-accessible', 'id': 'idServicio'}), required=False)
    class Meta:
        model = DetallePedidoServicio
        fields = ['idServicio', 'cantidad_servicios', 'descripcion', 'precio_inicial_servicio', 'subtotal_servicios']