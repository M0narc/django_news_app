from django.db import models
from django.utils import timezone
from apps.user_auth.models import CustomUser
from django.urls import reverse
from django.utils.text import slugify

# para poder hacer dinamica la categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'categorias'

    def get_absolute_url(self):
        return reverse("articulo:Categoria", kwargs={"slug": self.slug})

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs) 


class Articulo(models.Model):
    id = models.AutoField(primary_key=True, unique=True, editable = False)
    slug = models.SlugField(unique=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(null=False)
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, 
                                  null=True, 
                                  blank=True)
    fecha_publicada = models.DateField(default=timezone.now)
    imagen_portada = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("detalle_articulo", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs) 
