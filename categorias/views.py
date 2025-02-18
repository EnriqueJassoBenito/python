from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse

# Create your views here.

def agregar_categoria(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver')
        
    else:
        form = categoriaForm()
        
    return render(request, 'agregarCategorias.html', {'form': form})

def ver_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'ver-categoria.html', {'categoria':categorias})

def index(request):
    return render(request, 'categorias.html')

def lista_categoria(request):
    categorias = Categoria.objects.all()
    
    # generar un diccionario al aire que ordene los productos
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]
    
    return JsonResponse(data, safe=False)
