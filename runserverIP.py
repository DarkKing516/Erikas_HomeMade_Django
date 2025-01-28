# runserver_custom.py

import socket
import os

# Obtener la IP local
ip_local = socket.gethostbyname(socket.gethostname())
print(f"IP local detectada: {ip_local}")

# Path del archivo settings.py
settings_path = 'Erikas_HomeMade/settings.py'

# Leer el archivo settings.py
with open(settings_path, 'r') as file:
    settings = file.readlines()

# Buscar la línea de ALLOWED_HOSTS y actualizarla
for idx, line in enumerate(settings):
    if line.startswith('ALLOWED_HOSTS'):
        settings[idx] = f"ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '{ip_local}']\n"
        break

# Escribir los cambios en settings.py
with open(settings_path, 'w') as file:
    file.writelines(settings)

# Imprimir la URL de acceso al servidor
print(f"Accede al servidor desde: http://{ip_local}:8000/")

# Ejecutar el comando para iniciar el servidor de Django
os.system('python manage.py runserver 0.0.0.0:8000')
