from django.shortcuts import render, get_object_or_404
from .models import Categoria, Articulo

def home_view(request):
    categorias = Categoria.objects.all()
    articulos = Articulo.objects.all().order_by('-fecha_publicada')[:5]  # Últimos 5 artículos

    context = {
        'articulos': articulos,
        'categories': categorias,
    }
    
    return render(request, 'home.html', context)

def articulo_detalle(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    
    context = {
        'articulo': articulo,
    }
    
    return render(request, 'articulo/articulo.html', context)