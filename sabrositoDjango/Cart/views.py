from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

from sabrositoDjango.Cart.Carrito import Carrito

@login_required
def tienda(request):
    productos = Product.objects.all()
    return render(request, "02_tienda.html", {'productos':productos})



@login_required
def agregar_producto(request, product_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=product_id)
    carrito.agregar(producto,request)
    return redirect("menu")



@login_required
def eliminar_producto(request, product_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=product_id)
    carrito.eliminar(producto)
    return redirect("menu")
@login_required
def restar_producto(request, product_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=product_id)
    carrito.restar(producto)
    return redirect("menu")
@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("menu")


# Views para enviar productos al front
@login_required
def desayunos(request):
    productos = Product.objects.filter(category='Desayunos')
    return render(request, 'Desayunos.html', {'productos': productos})

@login_required
def almuerzos(request):
    productos = Product.objects.filter(category='Comidas')
    return render(request, 'Almuerzos.html', {'productos': productos})

@login_required
def jugos(request):
    productos = Product.objects.filter(category='Bebidas')
    return render(request, 'Jugos.html', {'productos': productos})


# Producto que el usuario elija
@login_required
def buscarUnProducto(request, product_name: str):
    producto = Product.objects.filter(name=product_name)
    return render(request, 'Producto.html', {'producto': producto})


# Agregar un producto y pagar
@login_required
def agregar_y_pagar(request, product_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=product_id)
    carrito.agregar(producto,request)
    return redirect("pagos")