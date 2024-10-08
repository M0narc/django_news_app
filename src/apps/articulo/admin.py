from django.contrib import admin
from .models import Articulo

class ArticuloCustomAdmin(admin.ModelAdmin):

    list_display = ('titulo', 
                    'autor', 
                    'fecha_publicada')

    # Habilitar búsqueda por título y nombre del autor
    search_fields = ('titulo', 
                     'autor__nombre', 
                     'autor__apellido')

    # Agregar filtros laterales por autor y fecha publicada
    list_filter = ('autor', 
                   'fecha_publicada')

    # Definir campos para el formulario de creación/edición
    fields = ('titulo', 
              'contenido', 
              'autor', 
              'fecha_publicada')

    # Agregar opción de ordenar los artículos por fecha publicada y título
    ordering = ('fecha_publicada', 
                'titulo')

admin.site.register(Articulo, ArticuloCustomAdmin)
