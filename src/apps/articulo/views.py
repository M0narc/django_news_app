from django.shortcuts import render
from .models import Categoria, Articulo

def home_view(request):
    categorias = Categoria.objects.all()
    articulos = Articulo.objects.all().order_by('-fecha_publicada')[:5]  # Últimos 5 artículos

    context = {
        'articulos': articulos,
        'categories': categorias,
    }
    
    return render(request, 'home.html', context)
