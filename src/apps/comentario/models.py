from django.db import models
from apps.user_auth.models import CustomUser
from apps.articulo.models import Articulo

# Create your models here.
class Comentario(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return f"Comentario de {self.autor} en {self.articulo}"
    