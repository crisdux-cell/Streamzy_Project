from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProductoRopa, PedidoRopa 

def home(request):
    # Trae todos los productos de la base de datos
    productos = ProductoRopa.objects.all() 
    return render(request, 'tienda/html.html', {'productos': productos})

@login_required
def admin_tienda(request):
    if not request.user.is_staff: 
        return redirect('home')
    pedidos = PedidoRopa.objects.all()
    return render(request, 'tienda/admin_dashboard.html', {'pedidos': pedidos})

@login_required
def agregar_producto(request):
    if not request.user.is_staff:
        return redirect('home')
    return render(request, 'tienda/agregar_producto.html')