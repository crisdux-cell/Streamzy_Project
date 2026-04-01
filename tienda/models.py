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
        # Añade esto al final de tu models.py actual
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

class ProductoRopa(models.Model): # Le puse Ropa para no confundir con Streamzy
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos_ropa/')
    stock = models.PositiveIntegerField(default=1)
    def __str__(self): return self.nombre

class PedidoRopa(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default='Pendiente')
    fecha = models.DateTimeField(auto_now_add=True)