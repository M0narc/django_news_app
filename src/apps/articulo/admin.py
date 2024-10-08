from django.contrib import admin
from .models import Articulo

# esto es un decorator
@admin.register(Articulo)
class ArticuloCustomAdmin(admin.ModelAdmin):

    list_display = ('titulo', 
                    'autor', 
                    'fecha_publicada')

    # busqueda por titulo y nombre del autor
    search_fields = ('titulo', 
                     'autor__nombre', 
                     'autor__apellido')

    # filtros laterales por autor y fecha publicada
    list_filter = ('autor', 
                   'fecha_publicada')

    # campos para el formulario de creación/edición
    fields = ('titulo', 
              'contenido', 
              'autor', 
              'fecha_publicada')

    # opcion de ordenar los articulos por fecha publicada y título
    ordering = ('fecha_publicada', 
                'titulo')
