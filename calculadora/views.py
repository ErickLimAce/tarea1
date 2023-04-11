from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, status
from rest_framework.response import Response
from . serializers import RetoSerializer,JugadorSerializer
from .models import Reto,Jugadores
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
import sqlite3 
import requests 
from random import randrange
from django.http import JsonResponse
from django.utils.decorators import method_decorator
import json
from django.views import View
from django.http import JsonResponse
# Create your views here.
def nueva():
    return 0
def index(request):
    #return HttpResponse("Bienvenido")
    return render(request,'index.html')

def procesamiento(request):
    nombre = request.POST['nombre']
    nombre = nombre.title()
    return render(request, 'proceso.html', {'name':nombre})

def lista(request):
    jugadores = Reto.objects.all() #select * from Reto 
    print(jugadores)
    return render(request, 'datos.html',{'lista_jugadores':jugadores})

def score(request):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    res = cur.execute("SELECT fecha,score FROM score")
    listado = res.fetchall()
    print(listado)
    return HttpResponse(listado)

@csrf_exempt
def usuarios(request):
    if request.method == 'GET':
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM usuarios")
        resultado = res.fetchall()
        lista =[]  
        for registro in resultado:
            id,grupo,grado,numero = registro
            diccionario = {"id":id,"grupo":grupo,"grado":grado,"num_lista":numero}
            lista.append(diccionario)
        #registros =[{"id":1,"grupo":"A","grado":6,"num_lista":4},{"id":2,"grupo":"B","grado":6,"num_lista":2}] 
        registros = lista
        return render(request, 'usuarios.html',{'lista_usuarios':registros})
    elif request.method == 'POST':
        body = request.body.decode('UTF-8')
        eljson = loads(body)
        grado = eljson['grado']
        grupo = eljson['grupo']
        num_lista = eljson['num_lista']
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES (?,?,?)",(grupo, grado, num_lista))
        con.commit()
        return HttpResponse('OK')
    elif request.method == 'DELETE':
        return(usuarios_d(request))
@csrf_exempt
def usuarios_p(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    grado = eljson['grado']
    grupo = eljson['grupo']
    num_lista = eljson['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("INSERT INTO usuarios (grupo, grado, num_lista) VALUES (?,?,?)",(grupo, grado, num_lista))
    con.commit()
    return HttpResponse('OK')

@csrf_exempt
def usuarios_d(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    id = eljson['id']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("DELETE FROM usuarios WHERE id_usuario=?",(str(id)))
    con.commit()
    return HttpResponse('OK usuario borrado'+str(id))

#servicio endpoint de validación de usuarios
#entrada: { "id_usuario" :"usuario","pass" : "contrasenia"}
#salida: {"estatus":True}
@csrf_exempt
def valida_usuario(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    usuario  = eljson['id_usuario']
    contrasenia = eljson['pass']
    print(usuario+contrasenia)
    #con = sqlite3.connect("db.sqlite3")
    #cur = con.cursor()
    #res = cur.execute("SELECT * FROM usuarios WHERE id_usuario=? AND password=?",(str(usuario),str(contrasenia)))
    #si el usuario es correcto regresar respuesta exitosa 200 OK
    #en caso contrario, regresar estatus false
    return HttpResponse('{"estatus":true}')

#Ruta para carga de la página web con el formulario de login
@csrf_exempt
def login(request):
    return render(request, 'login.html')

#Ruta para el proceso del login (invocación del servicio de verificación de usuario)
@csrf_exempt
def procesologin(request):
    usuario = request.POST['usuario']
    contrasenia = request.POST['password']
    #invoca el servicio de validación de usuario
    url = "http://127.0.0.1:8000/valida_usuario"
    header = {
    "Content-Type":"application/json"
    }
    payload = {   
    "id_usuario" :usuario,
    "pass" : contrasenia
    }
    result = requests.post(url,  data= dumps(payload), headers=header)
    if result.status_code == 200:
        return HttpResponse('Abrir página principal')
    return HttpResponse('Abrir página de credenciales inválidas')

class RetoViewSet(viewsets.ModelViewSet):
    queryset = Reto.objects.all()
    serializer_class = RetoSerializer
    
class JugadoresViewSet(viewsets.ModelViewSet):
    queryset = Jugadores.objects.all() #select * from Calculadora.Jugadores
    serializer_class = JugadorSerializer

def grafica(request):
    #h_var : The title for horizontal axis
    h_var = 'X'

    #v_var : The title for horizontal axis
    v_var = 'Y'

    #data : A list of list which will ultimated be used 
    # to populate the Google chart.
    data = [[h_var,v_var]]
    """
    An example of how the data object looks like in the end: 
        [
          ['Age', 'Weight'],
          [ 8,      12],
          [ 4,      5.5],
          [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
        ]
    The first list will consists of the title of horizontal and vertical axis,
    and the subsequent list will contain coordinates of the points to be plotted on
    the google chart
    """

    #The below for loop is responsible for appending list of two random values  
    # to data object
    for i in range(0,11):
        data.append([randrange(101),randrange(101)])

    #h_var_JSON : JSON string corresponding to  h_var
    #json.dumps converts Python objects to JSON strings
    h_var_JSON = dumps(h_var)

    #v_var_JSON : JSON string corresponding to  v_var
    v_var_JSON = dumps(v_var)

    #modified_data : JSON string corresponding to  data
    modified_data = dumps(data)

    #Finally all JSON strings are supplied to the charts.html using the 
    # dictiory shown below so that they can be displayed on the home screen
    return render(request,"charts.html",{'values':modified_data,\
        'h_title':h_var_JSON,'v_title':v_var_JSON})

def barras(request):
    '''
    data = [
          ['Jugador', 'Minutos Jugados'],
          ['Ian', 1000],
          ['Héctor', 1170],
          ['Alan', 660],
          ['Manuel', 1030]
        ]
    '''
    data = []
    data.append(['Jugador', 'Minutos Jugados'])
    resultados = Reto.objects.all() #select * from reto;
    titulo = 'Videojuego Odyssey'
    titulo_formato = dumps(titulo)
    subtitulo= 'Total de minutos por jugador'
    subtitulo_formato = dumps(subtitulo)
    if len(resultados)>0:
        for registro in resultados:
            nombre = registro.nombre
            minutos = registro.minutos_jugados
            data.append([nombre,minutos])
        data_formato = dumps(data) #formatear los datos en string para JSON
        elJSON = {'losDatos':data_formato,'titulo':titulo_formato,'subtitulo':subtitulo_formato}
        return render(request,'barras.html',elJSON)
    else:
        return HttpResponse("<h1> No hay registros a mostrar</h1>")
    
#Aquí empieza la tarea
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
import json
from .models import Usuario, Partida

class Usuarios(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    #get
    def get(self, request):
            users = list(Usuario.objects.values()) #Serializer en punto. Querryset  
            if len(users)>0:#valida que haya usuarios
                datos = {'users':users}
            else:
                datos = {'message':"No se enconteraron usuarios"}
            return JsonResponse(datos)
    #post      
    def post(self,request):
        jd = json.loads(request.body)
        Usuario.objects.create(password=jd['password'])#parametro contraseña
        datos = {'message': "Usuario creado correctamente"}
        return JsonResponse(datos)
    #put
    def put(self, request,id):
        jd = json.loads(request.body)
        users= list(Usuario.objects.filter(id=id).values())#Serializer en punto
        if len(users)>0:
            users=Usuario.objects.get(id=id) #recibe id
            users.password= jd['password']#nueva cont
            users.save()#guardo
            datos = {'message':"Se modifico correctamente"}
        else:
            datos = {'message':"Usuario erroneo, intentelo nuevamente"}
        return JsonResponse(datos)
    #delete
    def delete(self, request,id):
        users = list(Usuario.objects.filter(id=id).values()) #busca id
        if len(users)>0:
            Usuario.objects.filter(id=id).delete() #usa func delete
            datos = {'message':"Se eliminó correctamente"}
        else:
            datos = {'message':"No se encontró el usuario"}
        return JsonResponse(datos)

#para partidas es el mismo proceso
class Partidas(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
            partidas = list(Partida.objects.values()) #Serializer en punto
            if len(partidas)>0:
                datos = {'partidas':partidas}
            else:
                datos = {'message':"No se encontro la partida, intentelo nuevamente"}
            return JsonResponse(datos)
    
    def post(self,request):
        jd = json.loads(request.body)
        Partida.objects.create(fecha=jd['fecha'],id_usuario=Usuario.objects.get(pk = jd['id_usuario']),minutos_jugados=jd['minutos_jugados'],puntaje=jd['puntaje'])
        datos = {'message': "Partida añadida"}
        return JsonResponse(datos)
    
    def put(self, request,id):
        jd = json.loads(request.body)
        partidas= list(Partida.objects.filter(id=id).values())#Serializer en punto
        if len(partidas)>0:
            partidas=Partida.objects.get(id=id)
            partidas.fecha= jd['fecha']
            partidas.id_usuario= Usuario.objects.get(pk = jd['id_usuario'])
            partidas.minutos_jugados= jd['minutos_jugados']
            partidas.puntaje= jd['puntaje']
            partidas.save()
            datos = {'message':"Se modificó la partida"}
        else:
            datos = {'message':"No se encontro la partida"}
        return JsonResponse(datos)
    
    def delete(self, request,id):
        partidas = list(Partida.objects.filter(id=id).values())
        if len(partidas)>0:
            Partida.objects.filter(id=id).delete()
            datos = {'message':"Se elimino la partida"}
        else:
            datos = {'message':"No se encontro la partida"}
        return JsonResponse(datos)




