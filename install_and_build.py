import os
import subprocess

# Script para instalar dependencias y aplicar migraciones
# Crea el entorno virtual
print("Creando el entorno virtual...")
subprocess.run("python -m venv venv", shell=True)

# Activa el entorno virtual
print("Activando el entorno virtual...")
activate_command = os.path.join("venv", "Scripts", "activate") if os.name == "nt" else "source venv/bin/activate"
subprocess.run(activate_command, shell=True)

# Actualiza pip
print("Actualizando pip...")
subprocess.run("pip install --upgrade pip", shell=True)

# Instala las dependencias desde requirements.txt
print("Instalando dependencias...")
subprocess.run("pip install -r requirements.txt", shell=True)

# Aplica las migraciones
#print("Aplicando migraciones...")
#subprocess.run("python manage.py migrate", shell=True)

# Construye el frontend
print("Construyendo el frontend...")
frontend_dir = "sabrosito-react"
os.chdir(frontend_dir)
subprocess.run("npm install", shell=True)
subprocess.run("npm run build", shell=True)
os.chdir("..")

print("¡Instalación completa!")

# Inicia el servidor de Django
print("Iniciando el servidor de Django...")
subprocess.run("python manage.py runserver", shell=True)
