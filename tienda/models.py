from django.db import models

class Plantilla(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_preview = models.ImageField(upload_to='previews/')
    url_demo = models.URLField(max_length=500, blank=True, null=True)
    archivo_zip = models.FileField(upload_to='codigos_fuente/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre