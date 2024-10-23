from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from apps.comentario.models import Comentario
from .models import Categoria, Articulo
from apps.comentario.forms import ComentarioForm 
from django.utils import timezone
from django.views import View
from django.db.models import Q
from .forms import ArticuloForm
import logging


logger = logging.getLogger(__name__)


# funcion para crear articulo/posteo
def create_post(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES
        if form.is_valid():
            nuevo_articulo = form.save(commit=False)
            nuevo_articulo.autor = request.user  # Asignar el autor actual
            nuevo_articulo.save()  # Guardar el artículo en la base de datos
            return redirect('home')  # Redirigir a la página de inicio u otra página
    else:
        form = ArticuloForm()
    
    return render(request, 'articulo/crear_articulo.html', {'form': form})




class HomeView(ListView):
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


class ArticuloDetalleView(DetailView):
    model = Articulo
    template_name = 'articulo/articulo.html'
    context_object_name = 'articulo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articulo = self.object
        logger.info(f"Usuario {self.request.user} accedió al detalle del artículo {articulo.titulo}")
        context['comentarios'] = articulo.comentarios.all()
        context['form'] = ComentarioForm()
        
        # Comprobar si el usuario es colaborador o admin
        context['es_colaborador_o_admin'] = self.request.user.is_superuser or self.request.user.groups.filter(name='COLABORADOR').exists()
        
        # Obtener el comentario en edición si lo hay
        comentario_id = self.request.GET.get('editar', None)
        if comentario_id:
            logger.info(f"El usuario {self.request.user} está editando el comentario {comentario_id}")
            context['comentario_en_edicion'] = get_object_or_404(Comentario, id=comentario_id)
        
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        articulo = self.object

        # Procesar el formulario de edición del artículo
        if 'editar_articulo' in request.POST:
            logger.info(f"El usuario {request.user} está editando el artículo {articulo.titulo}")
            form_articulo = ArticuloForm(request.POST, instance=articulo)
            if form_articulo.is_valid():
                form_articulo.save()
                logger.info(f"Artículo {articulo.titulo} editado con éxito por {request.user}")
                return redirect('detalle_articulo', slug=articulo.slug)
            else:
                logger.warning(f"El formulario de edición de artículo no es válido para {articulo.titulo}")
                context = self.get_context_data()  # Obtiene el contexto
                context['form_articulo'] = form_articulo  # Agrega el formulario al contexto
                return self.render_to_response(context)
        
        # Procesar el formulario de comentario
        if 'editar_comentario' in request.POST:
            comentario_id = request.POST.get('comentario_id')
            comentario = get_object_or_404(Comentario, id=comentario_id)
            form_comentario = ComentarioForm(request.POST, instance=comentario)
            if form_comentario.is_valid():
                form_comentario.save()
                logger.info(f"Comentario editado con éxito por {request.user}")
                return redirect('detalle_articulo', slug=articulo.slug)
            else:
                logger.warning("Error al editar el comentario.")

        return self.get(request, *args, **kwargs)


class ComentarioView(View):
    def post(self, request, slug):
        articulo = get_object_or_404(Articulo, slug=slug)
        comentario_id = request.POST.get('comentario_id', None)

        # Si estamos editando un comentario
        if comentario_id:
            comentario = get_object_or_404(Comentario, id=comentario_id)
            if request.user == comentario.autor or request.user.is_superuser or request.user.groups.filter(name='COLABORADOR').exists():
                logger.info(f"Usuario {request.user} está editando el comentario {comentario_id}")
                form = ComentarioForm(request.POST, instance=comentario)
                if form.is_valid():
                    form.save()
                    return redirect('detalle_articulo', slug=articulo.slug)
                else:
                    logger.warning(f"El formulario de edición de comentario {comentario_id} no es válido")
        else:
            # Añadir nuevo comentario
            logger.info(f"Usuario {request.user} está añadiendo un nuevo comentario al artículo {articulo.titulo}")
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.articulo = articulo
                comentario.autor = request.user
                comentario.save()
                logger.info(f"Nuevo comentario añadido al artículo {articulo.titulo} por {request.user}")
                return redirect('detalle_articulo', slug=articulo.slug)
        
        return redirect('detalle_articulo', slug=articulo.slug)  # Redirigir en caso de error


class ArticuloUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm  # Asegúrate de tener este formulario creado
    template_name = 'articulo/articulo_form.html'
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  # Agregar todas las categorías al contexto
        return context

    def form_valid(self, form):
        # Manejar archivos correctamente al guardar el formulario
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        
        # Asegurarse de pasar request.FILES para manejar los archivos
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        """Redirige al detalle del artículo después de editar."""
        logger.info(f"Artículo {self.object.titulo} actualizado correctamente por {self.request.user}")
        return reverse_lazy('detalle_articulo', kwargs={'slug': self.object.slug})

    def test_func(self):
        """Permitir editar solo a autores, colaboradores o superusuarios."""
        articulo = self.get_object()
        is_authorized = (
            self.request.user == articulo.autor or 
            self.request.user.groups.filter(name='COLABORADOR').exists() or 
            self.request.user.is_superuser
        )
        if not is_authorized:
            logger.warning(f"Acceso denegado para la edición del artículo {articulo.titulo} por {self.request.user}")
        return is_authorized
    

class ArticuloDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = 'articulo/articulo_confirm_delete.html'  # Personaliza esta plantilla
    context_object_name = 'articulo'
    success_url = reverse_lazy('home')  # Redirige a la página principal después de eliminar

    def test_func(self):
        """Permitir eliminar solo a autores, colaboradores o superusuarios."""
        articulo = self.get_object()
        is_authorized = (
            self.request.user == articulo.autor or 
            self.request.user.groups.filter(name='COLABORADOR').exists() or 
            self.request.user.is_superuser
        )
        if not is_authorized:
            logger.warning(f"Acceso denegado para la eliminación del artículo {articulo.titulo} por {self.request.user}")
        return is_authorized
