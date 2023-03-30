from django.contrib import admin
from .models import Reto, Jugadores, Usuarios, Partidas_Jugador

# Register your models here.
admin.site.register(Reto)
admin.site.register(Jugadores)
admin.site.register(Usuarios)
admin.site.register(Partidas_Jugador)

