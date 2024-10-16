# user_auth/signals.py

from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from apps.articulo.models import Articulo
from apps.comentario.models import Comentario
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser

# Signal para asignar automáticamente el grupo MIEMBRO a nuevos usuarios
@receiver(post_save, sender=CustomUser)
def asignar_grupo_miembro(sender, instance, created, **kwargs):
    if created:  # Solo se ejecuta cuando el usuario es creado
        miembro_group, _ = Group.objects.get_or_create(name='MIEMBRO')
        instance.groups.add(miembro_group)

# Signal para crear grupos y asignar permisos después de la migración
@receiver(post_migrate)
def crear_grupos_y_permisos(sender, **kwargs):
    # Crear o obtener el grupo MIEMBRO
    miembro_group, _ = Group.objects.get_or_create(name='MIEMBRO')
    comentario_ct = ContentType.objects.get_for_model(Comentario)
    permisos_miembro = Permission.objects.filter(
        content_type=comentario_ct,
        codename__in=['add_comentario', 'change_comentario', 'delete_comentario']
    )
    miembro_group.permissions.set(permisos_miembro)

    # Crear o obtener el grupo COLABORADOR
    colaborador_group, _ = Group.objects.get_or_create(name='COLABORADOR')
    articulo_ct = ContentType.objects.get_for_model(Articulo)
    permisos_colaborador = Permission.objects.filter(
        content_type__in=[articulo_ct, comentario_ct]
    )
    colaborador_group.permissions.set(permisos_colaborador)
