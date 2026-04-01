from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.register),
    # Esta línea le dice a Django que las rutas están en la app 'tienda'
    path('', include('tienda.urls')), 
]

# Esto es para que las fotos de tus productos se vean en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)