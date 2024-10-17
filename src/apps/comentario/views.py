from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from .models import Comentario
from apps.articulo.models import Articulo
from apps.comentario.forms import ComentarioForm

def home_view(request):
    return render(request, 'comentario/home.html')

@login_required
def agregar_comentario(request, slug):
    articulo = get_object_or_404(Articulo, slug=slug)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.autor = request.user  
            comentario.save()
            return redirect('detalle_articulo', slug=articulo.slug) 
    else:
        form = ComentarioForm()
    return render(request, 'agregar_comentario.html', {'form': form, 'articulo': articulo})


class ComentarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comentario
    template_name = 'comentario/comentario_confirm_delete.html'  # Puedes personalizar este template
    success_url = reverse_lazy('lista_articulos')  # Cambia esta URL al destino deseado

    # Verificación de permisos: solo el autor, colaboradores o superusuarios pueden eliminar
    def test_func(self):
        comentario = self.get_object()
        return (self.request.user == comentario.autor or 
                self.request.user.groups.filter(name='COLABORADOR').exists() or 
                self.request.user.is_superuser)

    def get_success_url(self):
        """Redirige al detalle del artículo después de eliminar el comentario."""
        articulo = self.object.articulo
        return reverse_lazy('detalle_articulo', kwargs={'slug': articulo.slug})
