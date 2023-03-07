from django.shortcuts import render
from django.http import HttpResponse
from json import loads,dumps
from django.views.decorators.csrf import csrf_exempt

from .models import Reto
import sqlite3

class Fraccion:
    def __init__(self,num,den):
        self.num= num
        self.den= den
    def toJSON(self):
        return dumps(self,default=lambda o:o.__dict__,sort_keys=False,indent=4)
        
# Create your views here.
def nueva():
    return 0
def index(request):
    #return HttpResponse("Bienvenido")
    return render(request,'index.html')
def procesamiento(request):
    nombre = request.POST['nombre']
    nombre = nombre.title()
    return render(request,'proceso.html',{'name':nombre})
def lista(request):
    jugadores = Reto.objects.all()
    return render(request, 'datos.html',{'lista_jugadores':jugadores})

@csrf_exempt
def suma(request):
    print("Ingrese 2 fracciones para suma")
    body_unicode = request.body.decode('utf-8')
    body=loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']

    num2 = body['numerador2']
    den2 = body['denominador2']

    if(den1 == den2):
        num_r =num1+num2
        den_r =den1
    else: 
        num_r = (num1*den2)+(num2*den1)
        den_r = den1*den2
    
    resultado = Fraccion(num_r,den_r)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json,content_type ="text/json-comment-filtered")

@csrf_exempt
def resta(request):
    print("Ingrese 2 fracciones para resta")
    body_unicode = request.body.decode('utf-8')
    body=loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']

    num2 = body['numerador2']
    den2 = body['denominador2']

    if(den1 == den2):
        num_r =num1-num2
        den_r =den1
    else: 
        num_r = (num1*den2)-(num2*den1)
        den_r = den1*den2
    
    resultado = Fraccion(num_r,den_r)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json,content_type ="text/json-comment-filtered")

@csrf_exempt
def multiplicacion(request):
    print("Ingrese 2 fracciones para multi")
    body_unicode = request.body.decode('utf-8')
    body=loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']

    num2 = body['numerador2']
    den2 = body['denominador2']

    num_r =num1*num2
    den_r = den1*den2
    
    resultado = Fraccion(num_r,den_r)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json,content_type ="text/json-comment-filtered")

@csrf_exempt
def divison(request):
    print("Ingrese 2 fracciones para div")
    body_unicode = request.body.decode('utf-8')
    body=loads(body_unicode)
    num1 = body['numerador1']
    den1 = body['denominador1']

    num2 = body['numerador2']
    den2 = body['denominador2']

    num_r =num1*den2
    den_r = num2*den1
    
    resultado = Fraccion(num_r,den_r)
    resultado_json = resultado.toJSON()
    return HttpResponse(resultado_json,content_type ="text/json-comment-filtered")

"""def usuarios (request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res= cur.execute("SELECT * FROM usuarios")
    resultado = res.fetchall()
    for registro in resultado:
        [id,grupo, grado,numero]= registro
        print(registro)
    return HttpResponse(resultado)


def usuarios(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM usuarios")
    resultado = res.fetchall()
    registros = []
    for registro in resultado:
        [id, grupo, grado, numero] = registro
        registros.append({'id': id, 'grupo': grupo, 'grado': grado, 'numero': numero})
    return render(request, 'usuarios.html', {'registros': registros})

"""

@csrf_exempt
def usuarios(request):
    if request.method == 'GET':
        con = sqlite3.connect("db.sqlite3")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM usuarios")
        resultado = res.fetchall()
        con.close()
        return render(request, 'usuarios.html', {'resultado': resultado})
    elif request.method =='POST':
        return (usuarios_p(request))
    elif request.method=='DELETE':
        return (usuarios_d(request))
@csrf_exempt

def usuarios_p(request):
    body= request.body.decode('UTF-8')
    eljson=loads(body)
    grado=eljson['grado']
    grupo=eljson['grupo']
    num_lista=eljson['num_lista']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("INSERT INTO usuarios(grado,grupo,num_lista) VALUES (?,?,?)",(grupo,grado,num_lista))
    con.commit()
    return HttpResponse('OK')
@csrf_exempt
def usuarios_d(request):
    body= request.body.decode('UTF-8')
    eljson=loads(body)
    id_usuario=eljson['id_usuario']
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("DELETE FROM usuarios WHERE id_usuario = ?",(str(id_usuario)))
    con.commit()
    return HttpResponse('Borrado con exito')
   