from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from apps.comentario.models import Comentario
from .models import Categoria, Articulo
from apps.comentario.forms import ComentarioForm 
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import generic
from django.db.models import Q

class ArticuloSearchAndFilterView(ListView):
    model = Articulo
    template_name = 'home.html'
    context_object_name = 'articulos'

    def get_queryset(self):
        # Obtiene parámetros de búsqueda, filtro y ordenación desde los GET
        query = self.request.GET.get('q', '')  
        filtro = self.request.GET.get('filtro', None)
        orden = self.request.GET.get('orden', '-fecha_publicada')

        # Base queryset: artículos disponibles hasta la fecha actual
        queryset = Articulo.objects.filter(fecha_publicada__lte=timezone.now())

        # Aplicar filtro por categoría si existe
        if filtro:
            queryset = queryset.filter(categoria__nombre=filtro)

        # Aplicar búsqueda si se proporciona una query
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) | Q(categoria__nombre__icontains=query)
            ).distinct()

        # Aplicar ordenación según el parámetro recibido
        return queryset.order_by(orden)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega todas las categorías al contexto para el menú
        context['categories'] = Categoria.objects.all()

        # Mantener los valores actuales de búsqueda, filtro y orden en el contexto
        context['query_actual'] = self.request.GET.get('q', '')
        context['filtro_actual'] = self.request.GET.get('filtro', '')
        context['orden_actual'] = self.request.GET.get('orden', '-fecha_publicada')

        return context

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
