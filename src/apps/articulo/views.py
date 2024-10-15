from django.shortcuts import render, get_object_or_404, redirect
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

# class Categoria_vista(generic.ListView):
#     model = Articulo
#     template_name = 'home.html'

#     def get_queryset(self):
#         query = self.request.path.replace('/categoria/', '')
#         print(query)
#         articulos = Articulo.objects.filter(categoria__slug=query).filter(
#             fecha_publicada__lte=timezone.now()
#         )
#         return articulos

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Categoria.objects.all()
#         return context

class Categoria_vista(generic.ListView):
    model = Articulo
    template_name = 'articulo/resultados.html'  # Nueva plantilla para categorías

    def get_queryset(self):
        # Obtiene la categoría por su slug desde la URL
        categoria_slug = self.kwargs.get('slug')
        return Articulo.objects.filter(
            categoria__slug=categoria_slug,
            fecha_publicada__lte=timezone.now()
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categoria.objects.all()  # Para mostrar categorías en el menú
        context['categoria_actual'] = self.kwargs.get('slug')  # Mostrar la categoría actual si es necesario
        return context

class Resultado_vista(generic.ListView):
    model = Articulo
    template_name = 'articulo/resultados.html'

    def get_queryset(self):
        query = self.request.GET.get('Search...')
        articulos = Articulo.objects.filter(
            Q(titulo__icontains=query) | Q(categoria__nombre__icontains=query)
        ).filter(
            pub_date__lte=timezone.now()
        ).distinct()
        return articulos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categoria.objects.all()  # Para mostrar categorías en el menú
        context['categoria_actual'] = self.kwargs.get('slug')  # Mostrar la categoría actual si es necesario
        return context