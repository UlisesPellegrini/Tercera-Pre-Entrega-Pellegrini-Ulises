from django.db import models

# Create your models here.

class Paleta(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.descripcion} - {self.anio}'
    
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    informacion = models.TextField()
    
    def __str__(self):
        return f'{self.id} - {self.nombre} - {self.apellido} - {self.edad} - {self.informacion}'
    
    
class Auto(models.Model):
    marca = models.CharField(max_length=30)
    observacion = models.TextField()
    patente = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.observacion} - {self.patente}'