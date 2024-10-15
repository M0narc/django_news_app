from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campo para el avatar
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biografia = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', 
                                default='default_avatars/default_avatar.png', 
                                null=True, 
                                blank=True)

    # Definimos los roles o perfiles del usuario
    VISITANTE = 'visitante'
    MIEMBRO = 'miembro'
    COLABORADOR = 'colaborador'

    ROLE_CHOICES = [
        (MIEMBRO, 'Miembro o Usuario registrado'),
        (COLABORADOR, 'Colaborador'),
    ]

    # Campo para el perfil
    perfil = models.CharField(max_length=15, choices=ROLE_CHOICES, default=MIEMBRO)

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
