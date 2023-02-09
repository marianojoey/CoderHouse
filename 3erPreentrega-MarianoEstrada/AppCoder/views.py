from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from random import *

# Create your views here.

def inicio(request):
    return render(request,"AppCoder/inicio.html")
    #return HttpResponse ("Esta es la vista inicial")

def curso(request):
    
    if request.method == "POST":    #esto pasa si presiono el botón de enviar
        formulario=CursoFormulario(request.POST)
        
        if formulario.is_valid():
            info=formulario.cleaned_data
            """ esto es lo que usé inicialmente para cargar el formulario y grabarlo en la BD
            curso=Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
            """
            curso= Curso(nombre=info["curso"],camada=info["camada"])
            curso.save()
            return render(request, "AppCoder/cursos.html")
    
    else:   #esto es lo que pasa si no presiono el botón enviar
        formulario=CursoFormulario()
        
    return render (request, "AppCoder/cursos.html", {"formu":formulario})
    #return HttpResponse(f"El curso que he creado es {cur1.nombre}<br> de la camada {cur1.camada}") #se pueden usar comandos
    #de HTML en medio del texto. Por ejemplo <br> para saltar la línea.

def estudiante(request):
    if request.method == "POST":    #esto pasa si presiono el botón de enviar
        formulario=EstudFormul(request.POST)
        
        if formulario.is_valid():
            info=formulario.cleaned_data

            alumno= Estudiante(legajo=info["legajo"],nombre_apellido=info["nombre_apellido"],email=info["email"],cursando=info["cursando"],camada=info["camada"])
            alumno.save()
            return render(request, "AppCoder/estudiantes.html")
    
    else:   #esto es lo que pasa si no presiono el botón enviar
        formulario=EstudFormul()
        
    return render (request, "AppCoder/estudiantes.html", {"formu":formulario})

def profesor(request):
    if request.method == "POST":    #esto pasa si presiono el botón de enviar
        formulario=ProfesFormul(request.POST)
        
        if formulario.is_valid():
            info=formulario.cleaned_data

            profesor= Profesor(legajo=info["legajo"],nombre_apellido=info["nombre_apellido"],email=info["email"],curso_dictado=info["curso_dictado"])
            profesor.save()
            return render(request, "AppCoder/profesores.html")
    
    else:   #esto es lo que pasa si no presiono el botón enviar
        formulario=ProfesFormul()
        
    return render (request, "AppCoder/profesores.html", {"formu":formulario})

def resultadosCamada(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada) # __itcontains sirve para buscar cosas que contienen lo que
        #escribamos. Si queremos que la búsqueda sea EXACTA hay que usar __isexact
        return render (request,"AppCoder/cursos.html",{"cursos":cursos,"camada":camada})
    else:
        respuesta="No enviaste datos"
        
    return HttpResponse(respuesta)

def resultadosProfes(request):
    if request.GET["legajo"]:
        legajo = request.GET["legajo"]
        profes = Profesor.objects.filter(legajo__icontains=legajo)
                
        return render (request,"AppCoder/profesores.html",{"legajo":legajo,"profesores":profes})
    else:
        respuesta="No enviaste datos"
        
    return HttpResponse(respuesta)

def resultadosEstudiantes(request):
    if request.GET["legajo"]:
        legajo = request.GET["legajo"]
        alumnos = Estudiante.objects.filter(legajo__icontains=legajo) # __itcontains sirve para buscar cosas que contienen lo que
        #escribamos. Si queremos que la búsqueda sea EXACTA hay que usar __isexact
        return render (request,"AppCoder/estudiantes.html",{"legajo":legajo,"estudiante":alumnos})
    else:
        respuesta="No enviaste datos"
        
    return HttpResponse(respuesta)