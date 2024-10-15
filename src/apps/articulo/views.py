from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Articulo
from apps.comentario.forms import ComentarioForm 
from django.contrib.auth.decorators import login_required

def home_view(request):
    categorias = Categoria.objects.all()
    articulos = Articulo.objects.all().order_by('-fecha_publicada')[:5]  # Últimos 5 artículos

    context = {
        'articulos': articulos,
        'categories': categorias,
    }
    
    return render(request, 'home.html', context)

def articulo_detalle(request, articulo_id):  
    articulo = get_object_or_404(Articulo, id=articulo_id) 
    comentarios = articulo.comentarios.all()  

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.autor = request.user  
            comentario.save()
            return redirect('detalle_articulo', articulo_id=articulo.id)  
    else:
        form = ComentarioForm()

    context = {
        'articulo': articulo,
        'comentarios': comentarios,
        'form': form,  
    }
    
    return render(request, 'articulo/articulo.html', context)
