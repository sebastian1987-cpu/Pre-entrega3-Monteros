from django.shortcuts import render
from django.http import HttpResponse
from Games.models import *
from Games.forms import CursoFormulario

def Inicio(request):
    
    return render(request, "Games/inicio.html")

def games1(request):

    return render(request, "Games/games1.html")
def noticias(request):

    return render(request, "Games/noticias.html")

def contacto(request):
   
    if request.method == "POST":
        
        contact = CursoFormulario
        if contact.is_valid():
            info = contact.cleaned_data
            curso = Contacto1(nombre=info["curso"], camada=info["camada"])
        
        
            curso.save()

            return render(request, "Games/inicio.html")
        
    else:
        contact = CursoFormulario()

    return render(request, "Games/contacto.html", {"datos":contact})


        


   

    


# Create your views here.
