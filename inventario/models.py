from django.db import models

class Equipo(models.Model):
    tipo = models.CharField(max_length=100, db_index=True)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
 
    def __str__(self) -> str:
        return self.name