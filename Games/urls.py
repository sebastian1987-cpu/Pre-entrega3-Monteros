from django.urls import path
from Games.views import *

urlpatterns = [
    path('juegos/', games1),
    path('new/',noticias),
    path('inicio/',Inicio),
]