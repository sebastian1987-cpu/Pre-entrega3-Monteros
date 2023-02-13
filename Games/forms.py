from django import forms
from django.db import models

class CursoFormulario(forms.Form):

    curso = models.CharField(max_length=30)
    camada= models.CharField(max_length=40)
