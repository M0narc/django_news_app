from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from .models import Comentario
from apps.articulo.models import Articulo
from apps.comentario.forms import ComentarioForm
import logging


logger = logging.getLogger(__name__)


@login_required
def agregar_comentario(request, slug):
    logger.info("Intento de agregar comentario por el usuario: %s", request.user.username)
    articulo = get_object_or_404(Articulo, slug=slug)
    logger.debug("Artículo recuperado: %s", articulo)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.autor = request.user  
            comentario.save()
            logger.info("Comentario agregado correctamente por el usuario: %s en el artículo: %s", request.user.username, articulo.titulo)
            return redirect('detalle_articulo', slug=articulo.slug)
        else:
            logger.warning("Formulario de comentario inválido. Errores: %s", form.errors)
    else:
        form = ComentarioForm()
        logger.debug("Formulario de comentario vacío renderizado")

    return render(request, 'agregar_comentario.html', {'form': form, 'articulo': articulo})


class ComentarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comentario
    template_name = 'comentario/comentario_confirm_delete.html'  # Puedes personalizar este template
    success_url = reverse_lazy('lista_articulos')  # Cambia esta URL al destino deseado

    # Verificación de permisos: solo el autor, colaboradores o superusuarios pueden eliminar
    def test_func(self):
        comentario = self.get_object()
        if self.request.user == comentario.autor:
            logger.info("El usuario %s está autorizado para eliminar su propio comentario.", self.request.user.username)
            return True
        elif self.request.user.groups.filter(name='COLABORADOR').exists():
            logger.info("El usuario %s es colaborador y puede eliminar comentarios.", self.request.user.username)
            return True
        elif self.request.user.is_superuser:
            logger.info("El superusuario %s está eliminando un comentario.", self.request.user.username)
            return True
        else:
            logger.warning("El usuario %s no tiene permisos para eliminar el comentario.", self.request.user.username)
            return False
        
    def delete(self, request, *args, **kwargs):
        comentario = self.get_object()
        logger.info("Eliminando comentario: %s por el usuario: %s", comentario.id, request.user.username)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        """Redirige al detalle del artículo después de eliminar el comentario."""
        articulo = self.object.articulo
        logger.info("Comentario eliminado, redirigiendo al detalle del artículo: %s", articulo.titulo)
        return reverse_lazy('detalle_articulo', kwargs={'slug': articulo.slug})
    