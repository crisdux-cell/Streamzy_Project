from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProductoRopa, PedidoRopa  # Asegúrate de que estos nombres existan en models.py

def home(request):
    # Traemos los productos para mostrarlos en la página principal
    productos = ProductoRopa.objects.all() 
    # USAMOS 'html.html' PORQUE ASÍ SE LLAMA TU ARCHIVO
    return render(request, 'tienda/html.html', {'productos': productos})

@login_required
def admin_tienda(request):
    # Seguridad para que solo tú (Staff/Admin) puedas ver los pedidos
    if not request.user.is_staff: 
        return redirect('home')
    
    pedidos = PedidoRopa.objects.all()
    return render(request, 'tienda/admin_dashboard.html', {'pedidos': pedidos})

@login_required
def agregar_producto(request):
    # Seguridad para evitar que clientes agreguen productos
    if not request.user.is_staff:
        return redirect('home')
        
    return render(request, 'tienda/agregar_producto.html')