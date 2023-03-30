from rest_framework import serializers
from .models import Reto,Jugadores,Usuarios,Partidas_Jugador

class RetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reto
        fields = ('id','nombre','minutos_jugados')

class JugadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jugadores
        fields = ('id','grupo','num_lista')

def Serializer_Usuarios(Usuarios):
    return {
        'password': Jugadores.password,
        }
     
    
def Serializer_Partidas_Jugadores(Partidas_Jugador):
    return{
    'id':Partidas_Jugador.id,
    'fecha':Partidas_Jugador.fecha,
    'id_usuario':Partidas_Jugador.id_usuario,
    'minutos_jugados':Partidas_Jugador.minutos_jugados,
    'puntaje':Partidas_Jugador.puntaje,
    }
