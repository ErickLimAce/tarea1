from django.contrib import admin
from .models import Reto, Jugadores

# Register your models here.
admin.site.register(Reto)
admin.site.register(Jugadores)
#Aquí empieza la tarea
from django.contrib import admin
from .models import Usuario,PartidaJugador

# Register your models here.
admin.site.register(Usuario)
admin.site.register(PartidaJugador)

