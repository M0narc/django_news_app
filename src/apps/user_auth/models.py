from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campo para el avatar
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    # Definimos los roles o perfiles del usuario
    VISITANTE = 'visitante'
    MIEMBRO = 'miembro'
    COLABORADOR = 'colaborador'

    ROLE_CHOICES = [
        (VISITANTE, 'Visitante'),
        (MIEMBRO, 'Miembro o Usuario registrado'),
        (COLABORADOR, 'Colaborador'),
    ]

    # Campo para el perfil
    perfil = models.CharField(max_length=15, choices=ROLE_CHOICES, default=VISITANTE)

    # Solucionar los conflictos de 'groups' y 'user_permissions'
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Evitar el conflicto con el modelo auth.User
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Evitar el conflicto con el modelo auth.User
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username
