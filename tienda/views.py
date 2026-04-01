from django.shortcuts import render

def home(request):
    # Traemos todos los productos de la base de datos de Streamzy
    productos = ProductoRopa.objects.all() 
    return render(request, 'tienda/home.html', {'productos': productos})
    @login_required
def admin_tienda(request):
    if not request.user.is_staff: # Seguridad: solo tú o el dueño entran
        return redirect('home')
    pedidos = PedidoRopa.objects.all()
    return render(request, 'tienda/admin_dashboard.html', {'pedidos': pedidos})