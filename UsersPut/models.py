from django.db import models

# Create your models here.
class Viaje(models.Model):  #N viajes
    destino = models.CharField(max_length = 32)
    locomocion = models.CharField(max_length = 32)
    alojamiento = models.CharField(max_length = 32)
    precio = models.DecimalField(max_digits = 6, decimal_places = 2)
    def __str__(self):
        return self.destino
