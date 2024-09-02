from django.db import models
from geolocalizacion.models import Provincia, Localidad

class Cliente(models.Model): 
    razon_social = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True,  null=True)
    direccion = models.CharField(max_length=200, blank=True,  null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.razon_social}"
 


     
 

    
