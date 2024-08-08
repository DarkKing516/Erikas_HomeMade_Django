#!/usr/bin/env bash

while true
do
    # Realiza una solicitud HTTP a tu aplicación
    curl https://tu-app-en-render.com
    
    # Espera 40 minutos antes de hacer la siguiente solicitud
    sleep 2400
done
