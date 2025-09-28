from django.db import models

class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.TextField()
    motivo_de_visita = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_de_visita = models.DateField()

    def __str__(self):
        return self.nombre