from django.db import models
from geolocalizacion.models import Provincia, Localidad

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.username})"
 