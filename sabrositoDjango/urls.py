"""
URL configuration for sabrositoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .User import views
from .Pay import views as viewsPago
from .Cart import views as viewsCart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('AddSession', views.login_view, name='login'),
    path('Signup', views.register, name='signup'),
    path('menu', views.menu, name='menu'),
    path('info', views.info, name='info'),
    path('perfil', views.perfilPrueba, name='perfil'),
    path('pedidos', views.pedidos, name='pedidos'),


    #URLS PAY
    path('Paypal/', include('paypal.standard.ipn.urls')),
    path('pagos/',viewsPago.pago ,name='pagos'),
    path('paypal-return',viewsPago.paypal_return ,name='paypal-return'),
    path('paypal-cancel',viewsPago.paypal_cancel ,name='paypal-cancel'),


    #URLS DEL CARRITO
    path('tienda', viewsCart.tienda, name="Tienda"),
    path('agregar/<int:product_id>/', viewsCart.agregar_producto, name="agregar_al_carrito"),
    path('eliminar/<int:product_id>/', viewsCart.eliminar_producto, name="Del"),
    path('restar/<int:product_id>/', viewsCart.restar_producto, name="Sub"),
    path('limpiar/', viewsCart.limpiar_carrito, name="CLS"),
    #AGREGAR Y PAGAR
    path('agregarypagar/<int:product_id>/', viewsCart.agregar_y_pagar, name="addandpay"),


    #URLS DE PRODUCTOS
    path('desayunos', viewsCart.desayunos, name='desayunos'),
    path('almuerzos', viewsCart.almuerzos, name='almuerzos'),
    path('bebidas', viewsCart.jugos, name='bebidas'),


    #URL para buscar el producto que elija el usuario
    path('producto/<str:product_name>', viewsCart.buscarUnProducto, name='producto'),

    #LOGOUT
    path('cerrarsesion', views.cerrarsesion, name="cerrarsesion"),
]
