from django.shortcuts import render
from django.http import HttpResponse

def autor_view(request):
    return HttpResponse("Hola, probando respuesta desde la app autor")

