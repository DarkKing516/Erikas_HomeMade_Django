# Nombre del Proyecto

Breve descripción o introducción del proyecto.

## Recreación del Entorno Virtual y Reinstalación de Dependencias

Después de clonar este repositorio desde GitHub, sigue estos pasos para recrear el entorno virtual y reinstalar las dependencias del proyecto:

1. **Crear un Nuevo Entorno Virtual:**

   Utiliza la herramienta que prefieras para crear un nuevo entorno virtual. Por ejemplo, con `virtualenv`, puedes ejecutar el siguiente comando en tu terminal:
   ```
    pip install virtualenv
   ```

   ```
   virtualenv vnev
   ```
2. **Activar el Entorno Virtual:**

Una vez que el entorno virtual se haya creado, actívalo con el siguiente comando:
   ```
   .\vnev\Scripts\activate
   ```

3. **Instalar Django y las Dependencias:**

Con el entorno virtual activado, navega hasta la raíz de tu proyecto (donde se encuentra el archivo `requirements.txt` si tienes uno) y luego instala las dependencias utilizando `pip`:
   ```
   pip install django
   ```
   ```
   pip install -r requirements.txt
   ```

Si tienes un archivo `requirements.txt` que contiene todas las dependencias de tu proyecto, esto instalará todas las dependencias necesarias en tu entorno virtual.

Si quieres actualizar las dependecias porque agregaste más puedes usar:

   ```
   pip freeze > requirements.txt
   ```
