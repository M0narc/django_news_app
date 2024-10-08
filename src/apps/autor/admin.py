from django.contrib import admin
from.models import Autor

# Register your models here.

class AutorCustomAdmin(admin.ModelAdmin):

    # Muestra los campos principales en la lista de autores
    list_display = ('nombre', 
                    'apellido', 
                    'email', 
                    'fecha_creacion', 
                    'fecha_actualizacion')

    # Agrega barra de búsqueda para buscar por nombre, apellido o email
    search_fields = ('nombre', 
                     'apellido', 
                     'email')

    # Define los campos para crear/editar un autor
    fields = ('nombre', 
              'apellido', 
              'email', 
              'biografia')

    # Solo lectura para las fechas de creación y actualización
    readonly_fields = ('fecha_creacion', 
                       'fecha_actualizacion')

    # Opcionalmente, puedes agregar filtros laterales para filtrar por fecha de creación
    list_filter = ('fecha_creacion',)

admin.site.register(Autor, AutorCustomAdmin)