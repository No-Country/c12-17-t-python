from django.shortcuts import render, redirect
from .models import Product

# Create your views here.

from sabrositoDjango.Cart.Carrito import Carrito
from .models import Product


def tienda(request):
    productos = Product.objects.all()
    return render(request, "02_tienda.html", {'productos':productos})

def agregar_producto(request, product_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=product_id)
    carrito.agregar(producto,request)
    return redirect("Tienda")

def eliminar_producto(request, product_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=product_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, product_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=product_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")


# Views para enviar productos al front

def desayunos(request, slug_text):
    productos = Product.objects.filter(category='Desayunos', slug=slug_text)
    return render(request, 'Desayunos.html', {'productos': productos})

def almuerzos(request, slug_text):
    productos = Product.objects.filter(category='Comidas',slug=slug_text)
    return render(request, 'Almuerzos.html', {'productos': productos})

def jugos(request, slug_text):
    productos = Product.objects.filter(category='Bebidas', slug=slug_text)
    return render(request, 'Jugos.html', {'productos': productos})