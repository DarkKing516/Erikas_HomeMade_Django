---

# Erikas Home Made

Este proyecto se trata de [Breve descripción o introducción del proyecto].

## Configuración del Entorno Virtual y Reinstalación de Dependencias

Para configurar correctamente el entorno virtual y reinstalar las dependencias del proyecto después de clonar el repositorio desde GitHub, sigue estos pasos:

1. **Crear un Nuevo Entorno Virtual:**

   Utiliza tu herramienta preferida para crear un nuevo entorno virtual. Por ejemplo, si decides utilizar `virtualenv`, puedes instalarlo ejecutando el siguiente comando en tu terminal:
   
   ```
   pip install virtualenv
   ```

   Luego, crea un nuevo entorno virtual con el siguiente comando:
   
   ```
   virtualenv venv
   ```

2. **Activar el Entorno Virtual:**

   Una vez que el entorno virtual se haya creado con éxito, actívalo con el siguiente comando:
   
   ```
   .\venv\Scripts\activate
   ```

3. **Instalar Django y las Dependencias:**

   Con el entorno virtual activado, navega hasta la raíz de tu proyecto (donde se encuentra el archivo `requirements.txt`, si lo tienes) y luego instala las dependencias utilizando `pip`:
   
   ```
   pip install -r requirements.txt
   ```

   Si tienes un archivo `requirements.txt` que contiene todas las dependencias de tu proyecto, este comando instalará todas las dependencias necesarias en tu entorno virtual.

   Para actualizar el archivo `requirements.txt` con las nuevas dependencias que hayas añadido, puedes utilizar el siguiente comando: `pip freeze > requirements.txt`

   MIGRACIONES
   ```
   python manage.py makemigrations
   ```
   ```
   python manage.py migrate
   ```

---
## Estado de la Barra de Navegación

Generamos una variable local para la barra de navegación, así al ingresar la primera vez siempre veremos la barra de navegación abierta. Si la cerramos y vamos a otras pestañas, se quedará como la hayamos dejado, ya sea abierta o cerrada.

### Borrar la Variable de Estado

Si deseas borrar esa variable para que se resetee el estado de la barra de navegación, debes descomentar la siguiente línea de código y recargar la página:

```javascript
// localStorage.removeItem('sidebarState');
```

Este archivo se encuentra en la siguiente ruta:

`C:\Users\UwU\Documents\python_darkking\Erikas_HomeMade_Django\home\static\js\template.js`

**Recordar Siempre dejar esa línea comentada.**
