from django.contrib import admin
from django.urls import path
from tienda import views  # IMPORTANTE: Esto trae tus funciones de la carpeta tienda

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea es la que hace la magia:
    path('', views.home, name='home'), 
]
# En el urls.py de tu app
path('admin-tienda/', views.admin_tienda, name='admin_tienda'),
path('admin-tienda/agregar/', views.agregar_producto, name='agregar_producto'),