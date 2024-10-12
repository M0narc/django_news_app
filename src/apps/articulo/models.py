from django.db import models
from django.utils import timezone
from apps.user_auth.models import CustomUser

# para poder hacer dinamica la categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(null=False)
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, 
                                  null=True, 
                                  blank=True)
    fecha_publicada = models.DateField(default=timezone.now)
   
    def __str__(self):
        return self.titulo
