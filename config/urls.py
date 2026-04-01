from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ¡REVISA ESTA LÍNEA! Debe decir .site.urls
    path('admin/', admin.site.urls), 
    
    # Tu app principal
    path('', include('tienda.urls')),
]

# Para que se vean las imágenes de Streamzy en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)