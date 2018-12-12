from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tienda(models.Model):
    Nombre = models.CharField(max_length=255, null=False, blank=False)
    NombreSucursal = models.CharField(max_length=255)
    Direccion = models.TextField()
    Ciudad = models.CharField(max_length=255)
    Region = models.CharField(max_length=255)
    ESTADOS = (('P', 'Pendiente'), ('A', 'Aprobada'))
    Estado = models.CharField(max_length=1, choices=ESTADOS, default='P')

    def __str__(self):
        return self.Nombre

class Lista(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    NombreLista = models.CharField(null=False, blank=False, max_length=255, primary_key=True)
    ESTADOS = (('F', 'Finalizada'), ('I', 'Incompleta'))
    Estado = models.CharField(max_length=1, choices=ESTADOS, default='I')
    valorPresupuestado = models.IntegerField()
    costoReal = models.IntegerField()
    
    def __str__(self):
        return self.NombreLista
        
class Producto(models.Model):
    NombreProducto = models.CharField(null=False, blank=False, max_length=255)
    ValorProducto = models.IntegerField()
    Tienda = models.ForeignKey(Tienda, null=True, on_delete=models.CASCADE)
    Notas = models.TextField()
    ESTADOS = (('C', 'Comprado'), ('N', 'No Comprado'))
    Estado = models.CharField(max_length=1, choices=ESTADOS, default='N')
    Lista = models.ForeignKey(Lista, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.NombreProducto