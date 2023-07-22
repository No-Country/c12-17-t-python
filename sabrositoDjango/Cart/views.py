from django.shortcuts import render, redirect

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