from django.db import models

# Create your models here.
class Reto(models.Model):
    nombre = models.CharField(max_length= 30)
    minutos_jugados = models.IntegerField()

class Usuarios(models.Model):
    password = models.CharField(max_length=10)

class Jugadores(models.Model):
    grupo = models.CharField(max_length=2)
    num_lista = models.IntegerField()

class Partidas_Jugador(models.Model):
    fecha = models.DateField()
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE) 
    minutos_jugados = models.IntegerField()
    puntaje = models.IntegerField()