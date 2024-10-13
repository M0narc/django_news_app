from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comentario
from apps.articulo.models import Articulo
from apps.comentario.forms import ComentarioForm

def home_view(request):
    return render(request, 'comentario/home.html')

@login_required
def agregar_comentario(request, articulo_id):
    articulo = get_object_or_404(Articulo, id=articulo_id)
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
    return render(request, 'agregar_comentario.html', {'form': form, 'articulo': articulo})


@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if request.user == comentario.autor:  
        comentario.delete()
        return redirect('detalle_articulo', articulo_id=comentario.articulo.id)
    else:
        return redirect('detalle_articulo', articulo_id=comentario.articulo.id)
