from django.db import models
from django.contrib.auth.models import AbstractUser

class Autor(AbstractUser):
    email = models.EmailField(unique=True)
    biografia = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    foto_perfil = models.ImageField(
        upload_to="perfiles/",
        blank=True,
        null=False, 
        default="perfiles/default.jpg",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    username = None

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='autor_groups', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='autor_permissions', 
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
