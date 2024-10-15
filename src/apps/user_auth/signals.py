from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from apps.articulo.models import Articulo
from apps.comentario.models import Comentario

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Crear grupos
    miembro_group, created = Group.objects.get_or_create(name='MIEMBRO')
    colaborador_group, created = Group.objects.get_or_create(name='COLABORADOR')

    # Obtener permisos específicos para artículos y comentarios
    articulo_ct = ContentType.objects.get_for_model(Articulo)
    comentario_ct = ContentType.objects.get_for_model(Comentario)

    # Permisos para el grupo COLABORADOR
    permisos_colaborador = Permission.objects.filter(content_type__in=[articulo_ct, comentario_ct])
    colaborador_group.permissions.set(permisos_colaborador)

    # Permisos para el grupo MIEMBRO (solo agregar, modificar y eliminar comentarios)
    permisos_miembro = Permission.objects.filter(
        content_type=comentario_ct,
        codename__in=['add_comentario', 'change_comentario', 'delete_comentario']
    )
    miembro_group.permissions.set(permisos_miembro)
