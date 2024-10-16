from django.shortcuts import render, get_object_or_404, redirect

from apps.comentario.models import Comentario
from .models import Categoria, Articulo
from apps.comentario.forms import ComentarioForm 
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import generic
from django.db.models import Q

def home_view(request):
    categorias = Categoria.objects.all()
    articulos = Articulo.objects.all().order_by('-fecha_publicada')[:15]

    context = {
        'articulos': articulos,
        'categories': categorias,
    }
    
    return render(request, 'home.html', context)

@login_required
def articulo_detalle(request, slug):
    articulo = get_object_or_404(Articulo, slug=slug)
    comentarios = articulo.comentarios.all()

    es_colaborador_o_admin = request.user.is_superuser or request.user.groups.filter(name='COLABORADOR').exists()

    print("Es es_colaborador_o_admin -> ", request.user.groups)

    # Si hay un comentario en edición, obtener el comentario específico
    comentario_en_edicion = None
    comentario_id = request.GET.get('editar', None)
    if comentario_id:
        comentario_en_edicion = get_object_or_404(Comentario, id=comentario_id)

    if request.method == 'POST':
        comentario_id = request.POST.get('comentario_id', None)
        
        # Si estamos editando un comentario
        if comentario_id:
            comentario = get_object_or_404(Comentario, id=comentario_id)
            if request.user == comentario.autor or es_colaborador_o_admin:
                form = ComentarioForm(request.POST, instance=comentario)
                if form.is_valid():
                    form.save()
                    return redirect('detalle_articulo', slug=articulo.slug)
        else:
            # Añadir nuevo comentario
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.articulo = articulo
                comentario.autor = request.user
                comentario.save()
                return redirect('detalle_articulo', slug=articulo.slug)
    else:
        form = ComentarioForm()

    context = {
        'articulo': articulo,
        'comentarios': comentarios,
        'form': form,
        'es_colaborador_o_admin': es_colaborador_o_admin,
        'comentario_en_edicion': comentario_en_edicion,  # Para saber si hay un comentario en edición
    }

    return render(request, 'articulo/articulo.html', context)

# http://127.0.0.1:8000/articulo/qa-stuff

class Categoria_vista(generic.ListView):
    model = Articulo
    template_name = 'articulo/resultados.html' 

    def get_queryset(self):
        categoria_slug = self.kwargs.get('slug')
        return Articulo.objects.filter(
            categoria__slug=categoria_slug,
            fecha_publicada__lte=timezone.now()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categoria.objects.all()  
        context['categoria_actual'] = self.kwargs.get('slug')  
        return context

class Resultado_vista(generic.ListView):
    model = Articulo
    template_name = 'articulo/resultados.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')  
        if query:  # Verifica que haya contenido en query
            return Articulo.objects.filter(
                Q(titulo__icontains=query) | Q(categoria__nombre__icontains=query),
                fecha_publicada__lte=timezone.now()
            ).distinct()
        else:
            return Articulo.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categoria.objects.all()  # Para mostrar categorías en el menú
        context['categoria_actual'] = self.kwargs.get('slug')  # Mostrar la categoría actual si es necesario
        return context