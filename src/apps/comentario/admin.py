from django.contrib import admin
from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    
    list_display = (
        'autor',
        'contenido',
        'fecha_creacion',
    )
    
    list_filter = (
        'autor',
        'fecha_creacion',
        
    )
    
    search_fields = (
        'autor__nombre',
        'contenido',
    )
    
    ordering = [
        'fecha_creacion'
    ]
