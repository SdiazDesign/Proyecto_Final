from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from App.models import *
from App.forms import *

def home(request): 

    info = {}
    
    return render(request, "home.html", info)

def crear_partido(request): 
    
    info = {
        "equipos" : Equipos.objects.all() 
    }

    return render(request, "crear_partido.html", info)

def crear_equipo(request): 
    
    info = {}

    return render(request, "crear_equipo.html", info)

def crear_resultado(request): 

    partidos = Partidos.objects.select_related('equipo_local', 'equipo_visitante')

    info = {
        "partidos" : partidos 
    }

    return render(request, "crear_resultado.html", info)

def grabar_equipo(request): 
    
    if request.method == "POST":

        form = EquiposForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            
            equipo = Equipos(
                nombre = info["nombre"],
                fechafundacion = info["fechafundacion"]
            )

            equipo.save()

    return render(request, "home.html")

def grabar_partido(request): 
    
    if request.method == "POST":

        form = PartidosForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data

            partido = Partidos(
                equipo_local = info["equipo_local"],
                equipo_visitante = info["equipo_visitante"],
                fecha = info["fecha"],
                hora = info["hora"]
            )

            partido.save()

    return render(request, "home.html")

def grabar_resultado(request): 

    if request.method == "POST":

        form = ResultadosForm(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data

            resultado = Resultados(
                partido = info["partido"],
                equipo_local = info["equipo_local"],
                equipo_visitante = info["equipo_visitante"]
            )

            resultado.save()

    return render(request, "home.html")

def get_resultado(request):

    id = request.GET["partido"]

    if id:
        
        # resultado = Resultados.objects.filter(id__iexact=id).values()
        resultado = Resultados.objects.filter(id__iexact=id)[0]

        info = {
            "id" : id,
            "resultado" : resultado,
        }

        return render(request, "get_resultado.html", info)
    
    else : 

        response = "No enviaste datos"

        return HttpResponse(response)

def buscar_resultado(request):

    partidos = Partidos.objects.select_related('equipo_local', 'equipo_visitante')

    info = {
        "partidos" : partidos 
    }

    return render(request, "buscar_resultado.html", info)

    
    
    
