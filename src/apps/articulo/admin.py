from django.contrib import admin
from .models import Articulo, Categoria

@admin.register(Articulo)
class ArticuloCustomAdmin(admin.ModelAdmin):

    list_display = ('titulo', 
                    'autor', 
                    'categoria',
                    'fecha_publicada')

    # buscar por titulo, nombre del autor y categoría
    search_fields = ('titulo', 
                     'autor__nombre', 
                     'autor__apellido',
                     'categoria__nombre')

    # Filtros laterales por autor, fecha publicada y categoría
    list_filter = ('autor', 
                   'fecha_publicada',
                   'categoria')

    # formulario de creación/edición
    fields = ('titulo', 
              'contenido', 
              'autor', 
              'categoria',  # Agregar la categoría en el formulario
              'fecha_publicada')

    # opcion de ordenar los artículos por fecha publicada y título
    ordering = ('fecha_publicada', 
                'titulo')

@admin.register(Categoria)
class CategoriaCustomAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    # para poder crear las nuevas categorias
    fields = ('nombre',)