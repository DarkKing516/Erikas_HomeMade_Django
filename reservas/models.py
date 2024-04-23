from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from usuarios.models import Usuario  # Importa el modelo de usuarios

def validate_fecha_hoy(value):
    if value.date() != timezone.now().date():
        raise ValidationError('La fecha debe ser la del día de hoy')

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con la tabla de usuarios
    fecha = models.DateTimeField(validators=[validate_fecha_hoy])
    fecha_cita = models.DateTimeField()
    descripcion = models.CharField(max_length=80, null=True, blank=True)
    estado = models.CharField(max_length=80, default="Pendiente")

    def __str__(self):
        return f"Reserva {self.id}"
    
    class Meta:
        db_table = 'reservas'  # Personalizando el nombre de la tabla
