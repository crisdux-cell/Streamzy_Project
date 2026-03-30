from django.shortcuts import render

def home(request):
    # Ya no pongas 'ventas/', solo el nombre del archivo
    return render(request, 'html.html')