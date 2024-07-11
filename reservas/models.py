from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from usuarios.models import Usuario  # Importa el modelo de usuarios

def validate_fecha_hoy(value):
    if value.date() != timezone.now().date():
        raise ValidationError('La fecha debe ser la del día de hoy')

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    fecha_cita = models.DateTimeField()
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=80, default="Pendiente")

    def __str__(self):
        return f"Reserva {self.id}"

    def clean(self):
        if self.fecha_cita < self.fecha:
            raise ValidationError(_("La fecha de la cita no puede ser anterior a la fecha de la reserva."))

    class Meta:
        db_table = 'reservas'