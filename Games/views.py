from django.shortcuts import render
from django.http import HttpResponse
from Games.models import *

def games1(request):
    Juegos = Games1(nombre = "Resident evil 4", plataforma="ps5", desarrolladora="Capcom", año= 2023)
    Juegos.save()
    
    return HttpResponse(f"El proximo juego que se estrena el {Juegos.año} sera {Juegos.nombre} para la {Juegos.plataforma}")

def noticias(request):

    noti= News(titulo = "Nuevo remake de RE", fecha = 2023, genero = "survival horror")
    noti.save()

    return HttpResponse(f"Capcom tiene un {noti.titulo} que saldra {noti.fecha}, un ya conocido {noti.genero}")


def Inicio(request):
    
    return render(request, "Games/inicio.html")

# Create your views here.
