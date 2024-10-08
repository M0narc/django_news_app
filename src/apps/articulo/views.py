from django.shortcuts import render
from .models import Articulo

def home_view(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicada')[:5]  # Últimos 5 artículos
    return render(request, 'home.html', {'articulos': articulos})
