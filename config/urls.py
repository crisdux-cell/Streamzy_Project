from django.contrib import admin
from django.urls import path
from tienda import views  # IMPORTANTE: Esto trae tus funciones de la carpeta tienda

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea es la que hace la magia:
    path('', views.home, name='home'), 
]