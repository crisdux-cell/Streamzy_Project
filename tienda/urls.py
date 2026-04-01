from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-tienda/', views.admin_tienda, name='admin_tienda'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
]