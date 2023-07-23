from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

from django.contrib.auth.models import User 
from .models import info_extra_usuario as DataUser

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
                    return redirect('perfil')
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
            


        

def menu(request):
    if request.method == 'GET':
        return render(request, 'menu.html')

def comidas(request):
    if request.method == 'GET':
        return render(request, 'Opciones.html')
    
def producto(request):
    if request.method == 'GET':
        return render(request, 'Producto.html')

def pagos(request):
    if request.method == 'GET':
        return render(request, 'pagos.html')
    
def perfilPrueba(request):
    if request.method == 'GET':
        return render(request, 'perfil.html')
    
def perfil(request):
    userLog = request.user
    if request.method == 'GET':
        return render(request, 'perfil.html', {'username': userLog.username})
    else: 
        newDataUser = DataUser(user=userLog, phone= request.POST['phone'], address=request.POST['address'])
        newDataUser.save()
        return redirect('menu')