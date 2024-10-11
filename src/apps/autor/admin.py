from django.contrib import admin
from.models import Autor

# el @ es un decorator

@admin.register(Autor)
class AutorCustomAdmin(admin.ModelAdmin):

    # Muestra los campos principales en la lista de autores
    list_display = ('first_name', 
                    'last_name', 
                    'email', 
                    'fecha_creacion', 
                    'fecha_actualizacion')

    # Agrega barra de búsqueda para buscar por first_name, last_name o email
    search_fields = ('first_name', 
                     'last_name', 
                     'email')

    # Define los campos para crear/editar un autor
    fields = ('first_name', 
              'last_name', 
              'email', 
              'biografia')

    # Solo lectura para las fechas de creación y actualización
    readonly_fields = ('fecha_creacion', 
                       'fecha_actualizacion')

    # Opcionalmente, puedes agregar filtros laterales para filtrar por fecha de creación
    list_filter = ('fecha_creacion',)
