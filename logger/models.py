from django.db import models

class Logs(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # Fecha y hora automáticas
    endpoint = models.CharField(max_length=255, null=True, blank=True)  # El endpoint de la API
    input_data = models.TextField(null=True, blank=True)  # Datos de entrada (pueden ser JSON, texto, etc.)
    output_data = models.TextField(null=True, blank=True)  # Datos de salida (pueden ser JSON, texto, etc.)
    code = models.TextField(null=True, blank=True)  # Código de estado (puede ser texto, número, etc.)

    def __str__(self):
        return f"{self.timestamp} - {self.endpoint}"