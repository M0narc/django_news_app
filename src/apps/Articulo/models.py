from django.db import models
from django.utils import timezone
from apps.autor.models import Autor

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicada = models.DateField(default=timezone.now)
   
    def __str__(self):
        return self.titulo
    