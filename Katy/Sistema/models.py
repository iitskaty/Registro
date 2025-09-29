from django.db import models

class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    motivo_de_visita = models.CharField(max_length=256,default="")
    fecha_de_visita = models.DateField()

    def __str__(self):
        return self.nombre