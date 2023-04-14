from django.urls import include,path
from rest_framework import routers
from . import views

#Tarea
from .views import Partidas, Usuarios
#Tarea tabla
from .views import Tabla



router = routers.DefaultRouter()
router.register(r'reto', views.RetoViewSet)
router.register(r'jugador', views.JugadoresViewSet)


urlpatterns = [
    path('api',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',views.index, name='index'),
    path('procesamiento', views.procesamiento, name='procesamiento'),
    path('lista',views.lista,name='lista'),
    path('score',views.score,name='score'),
    #path('usuarios',views.usuarios,name='usuarios'),
    path('usuarios_p',views.usuarios_p,name='usuarios_p'),
    path('usuarios_d',views.usuarios_d, name='usuarios_d'),
    path('login', views.login, name='login'),
    path('procesologin', views.procesologin, name='procesologin'),
    path('valida_usuario',views.valida_usuario,name='valida_usuario'),
    path('grafica',views.grafica,name='grafica'),
    path('barras',views.barras,name='barras'),
    
    
    path('partidas',  Partidas.as_view(),name='Partidas'),
    path('partidas/<int:id>',  Partidas.as_view(),name='Partida'),
    path('usuarios',  Usuarios.as_view(),name='Partidas'),
    path('usuarios/<int:id>',  Usuarios.as_view(),name='Partida'),
    

   path('tabla',  Tabla.as_view(),name='Tabla'),
]

#Para correrlo usando RESTMAN debemos: En la sección "Headers",  incluir "Content-Type" y "application/json" y posteriormente escribir el formato json en seccion raw
#Como ejemplo Para partidas por jugador: {"fecha": "2022-03-30","id_usuario": 22,"minutos_jugados": 30,"puntaje": 100} Si no existe un usario con el id no te permitirá crear una partida
#Para DELETE http://ip:8000/usuarios/22 
#En el caso de partidas
#Para PUT http://ip:8000/usuarios/21 y json "password": 12345}
#En el caso de Partidas http://ip:8000/partidasjugador/5 5 siendo el id de la partida { "fecha": "2022-03-29","id_usuario": 21,"minutos_jugados": 120,"puntaje": 80}


