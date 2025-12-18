from django.db import models
from django.utils import timezone

class Visita(models.Model):
    nombre_visitante = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, help_text="Formato: 12.345.678-9")
    motivo = models.TextField()
    empresa_procedencia = models.CharField(max_length=100, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)  # Se marca solo al crear
    fecha_salida = models.DateTimeField(null=True, blank=True) # Se llena al salir

    def __str__(self):
        return f"{self.nombre_visitante} - {self.rut}"

    class Meta:
        verbose_name = "Visita"
        verbose_name_plural = "Registro de Visitas"
        ordering = ['-fecha_ingreso']