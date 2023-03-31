from rest_framework import serializers
from .models import Reto,Jugadores

class RetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reto
        fields = ('id','nombre','minutos_jugados')

class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('id','grupo','num_lista')

#aqui empieza la tarea
from rest_framework import serializers
from .models import Usuario, PartidaJugador

class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = '__all__'

class PartidaJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidaJugador
        fields = '__all__'