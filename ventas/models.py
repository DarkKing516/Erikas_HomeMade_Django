from django.db import models
from pedidos.models import Pedido  # Importa el modelo de pedidos

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    idPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.idVenta}"
