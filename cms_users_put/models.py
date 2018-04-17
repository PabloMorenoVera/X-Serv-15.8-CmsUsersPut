from django.db import models

# Create your models here.
class Page(models.Model):
    direccion = models.CharField(max_length = 128)
    dir_acortada = models.CharField(max_length = 128)
    def __str__(self):
        return self.direccion
