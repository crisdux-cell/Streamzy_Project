from django.contrib import admin
from .models import ProductoRopa, PedidoRopa

# Registro simple y directo
admin.site.register(ProductoRopa)
admin.site.register(PedidoRopa)