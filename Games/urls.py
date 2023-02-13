from django.urls import path
from Games.views import *

urlpatterns = [
    path('contacto/',contacto, name="Contacto"),
    path('juegos/', games1, name="Juegos"),
    path('new/',noticias, name= "New"),
    path('inicio/',Inicio, name="Inicio"),
       
]