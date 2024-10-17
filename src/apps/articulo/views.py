from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from apps.comentario.models import Comentario
from .models import Categoria, Articulo
from apps.comentario.forms import ComentarioForm 
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View, generic
from django.db.models import Q

class home_view(ListView):
    model = Articulo
    template_name = 'home.html'
    context_object_name = 'articulos'
    ordering = '-fecha_publicada'  # Orden predeterminado
    
    def get_queryset(self):
        # Obtenemos el parámetro de orden de la URL, si existe
        orden = self.request.GET.get('orden', '-fecha_publicada')
        
        # Devolvemos los artículos ordenados según el parámetro recibido
        return Articulo.objects.all().order_by(orden)[:15]

    def get_context_data(self, **kwargs):
        # Agregamos las categorías al contexto
        context = super().get_context_data(**kwargs)
        context['categories'] = Categoria.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class ArticuloDetalleView(DetailView):
    model = Articulo
    template_name = 'articulo/articulo.html'
    context_object_name = 'articulo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articulo = self.object
        context['comentarios'] = articulo.comentarios.all()
        context['form'] = ComentarioForm()
        
        # Comprobar si el usuario es colaborador o admin
        context['es_colaborador_o_admin'] = self.request.user.is_superuser or self.request.user.groups.filter(name='COLABORADOR').exists()
        
        # Obtener el comentario en edición si lo hay
        comentario_id = self.request.GET.get('editar', None)
        if comentario_id:
            context['comentario_en_edicion'] = get_object_or_404(Comentario, id=comentario_id)
        
        return context

class ComentarioView(View):
    def post(self, request, slug):
        articulo = get_object_or_404(Articulo, slug=slug)
        comentario_id = request.POST.get('comentario_id', None)

        # Si estamos editando un comentario
        if comentario_id:
            comentario = get_object_or_404(Comentario, id=comentario_id)
            if request.user == comentario.autor or request.user.is_superuser or request.user.groups.filter(name='COLABORADOR').exists():
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
        
        return redirect('detalle_articulo', slug=articulo.slug)  # Redirigir en caso de error


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

class Resultado_vista(ListView):
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
    

def orden_nuevo(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicada')[:15]