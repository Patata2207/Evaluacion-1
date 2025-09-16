from django.db import models

class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12) 
    motivo = models.TextField()
    hora_entrada = models.DateTimeField()  # sin auto_now_add

    hora_salida = models.DateTimeField()  

    def __str__(self):
        return f"{self.nombre} ({self.rut})"
