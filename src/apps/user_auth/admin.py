from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Definir los campos que se mostrarán en la lista de usuarios
    list_display = ('username', 
                    'email', 
                    'first_name', 
                    'last_name', 
                    'perfil', 
                    'is_staff')

    # Definir los filtros laterales
    list_filter = ('perfil', 
                   'is_staff', 
                   'is_superuser', 
                   'is_active', 
                   'groups')

    # Campos que se pueden buscar
    search_fields = ('username', 
                     'email', 
                     'first_name', 
                     'last_name')

    # Para que los usuarios puedan asignar roles y demás campos adicionales
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': 
                                  ('first_name', 
                                   'last_name', 
                                   'email', 
                                   'biografia', 
                                   'avatar')}),
        ('Permisos', {'fields': 
                      ('is_active', 
                       'is_staff', 
                       'is_superuser', 
                       'groups', 
                       'user_permissions')}),
        ('Perfiles y Roles', {'fields': ('perfil',)}),  # Campo personalizado para el perfil
        ('Fechas Importantes', {'fields': 
                                ('last_login', 
                                 'date_joined')}),
    )

    # Para el formulario de creación de usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'perfil', 'is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
    )

    ordering = ('username',)  # Orden por defecto de la lista

# Registrar el modelo CustomUser con el CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
