from django.urls import include,path
from rest_framework import routers
from . import views
#Tarea
from .views import UsuarioList, UsuarioDetail, PartidaJugadorList, PartidaJugadorDetail
#prueba



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
    path('usuarios',views.usuarios,name='usuarios'),
    path('usuarios_p',views.usuarios_p,name='usuarios_p'),
    path('usuarios_d',views.usuarios_d, name='usuarios_d'),
    path('login', views.login, name='login'),
    path('procesologin', views.procesologin, name='procesologin'),
    path('valida_usuario',views.valida_usuario,name='valida_usuario'),
    path('grafica',views.grafica,name='grafica'),
    path('barras',views.barras,name='barras'),
    
    
    
    path('usuarios/', UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuario-detail'),
    path('partidasjugador/', PartidaJugadorList.as_view(), name='partidajugador-list'),
    path('partidasjugador/<int:pk>/', PartidaJugadorDetail.as_view(), name='partidajugador-detail'),
]

#Para correrlo debemos: En la sección "Headers",  incluir "Content-Type" y "application/json" y posteriormente escribir el formato json en seccion raw
#Como ejemplo Para partidas por jugador: {"fecha": "2022-03-30","id_usuario": 22,"minutos_jugados": 30,"puntaje": 100} Si no existe un usario con el id no te permitirá crear una partida
#Para DELETE http://localhost:8000/usuarios/22 y {"id": 22} no pude generarlo solo desde el json
#En el caso de partidas
#Para PUT http://localhost:8000/usuarios/21 y json {"id": 21, "password": 12345}, de igual forma no pude hacer que buscara el id sin especificarlo en la url.
#En el caso de Partidas http://localhost:8000/partidasjugador/5 5 siendo el id de la partida { "id": 5,"fecha": "2022-03-29","id_usuario": 21,"minutos_jugados": 120,"puntaje": 80}
#Sin embargo tanto para DELETe como PUT generé una verificación que permitiera borrar/actualizar tanto usuarios como partidas por medio del ID y dependiendo el caso te desplegaría un mensaje correspondiente

