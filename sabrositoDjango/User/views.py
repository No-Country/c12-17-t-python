from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.http import  HttpResponseRedirect
from django.contrib.auth.models import User
from .models import info_extra_usuario as DataUser
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'Registro.html')
    else:
        if request.method == 'POST':
            existsUser = User.objects.filter(username = request.POST["username"]).first()
            existsEmail = User.objects.filter(email = request.POST["email"]).first()
            if request.POST["password1"] == request.POST["password2"]:
                if existsUser:
                    return render(request, 'Registro.html', {'error': 'El nombre de usuario ingresado ya existe'})
                elif existsEmail:
                    return render(request, 'Registro.html', {'error': 'El email ingresado está en uso'})
                else:
                    createUser = User.objects.create(username = request.POST["username"], email = request.POST["email"])
                    createUser.set_password(request.POST["password1"])
                    createUser.save()
                    login(request, createUser)
                    contenido = "Usuario creado exitosamente."
                    return HttpResponse(contenido, status=200)
            else:
                return render(request, 'Registro.html', {"error": "Las contraseñas no coinciden."})



def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        searchUser = User.objects.filter(email=request.POST['email']).first()
        if searchUser:
            password_plain = request.POST['password']
            password_hashed = searchUser.password

            password_matched = check_password(password_plain, password_hashed)

            try:
                if password_matched:
                    login(request, searchUser)
                    return redirect('menu')
                else:
                    return render(request, 'login.html', {'error': 'Las contraseñas no coinciden'})
            except:
                return render(request, 'login.html', {'error': 'Algo salió mal, intentelo nuevamente o contacte al soporte'})
        else:
            return render(request, 'login.html', {'error': 'El email ingresado no existe'})




@login_required
def menu(request):
    if request.method == 'GET':
        return render(request, 'menu.html')

@login_required
def pedidos(request):
    if request.method == 'GET':
        return render(request, 'Pedidos.html')

@login_required
def info(request):
    if request.method == 'GET':
        return render(request, 'InfoMenu.html')

@login_required
def perfilPrueba(request):
    if request.method == 'GET':
        return render(request, 'perfil.html')

@login_required
def perfil(request):
    userLog = request.user
    if request.method == 'GET':
        return render(request, 'perfil.html', {'username': userLog.username})
    else:
        newDataUser = DataUser(user=userLog, phone= request.POST['phone'], address=request.POST['address'])
        newDataUser.save()
        return HttpResponseRedirect('menu')


def cerrarsesion(request):
    logout(request)
    return redirect('index')


