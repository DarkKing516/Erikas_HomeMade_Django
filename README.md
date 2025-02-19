# 🏡 Erikas Home Made 🍪

¡Bienvenido a **Erikas Home Made**! Un proyecto dedicado a [breve descripción o introducción del proyecto]. Aquí encontrarás todo lo necesario para explorar y disfrutar de nuestra plataforma.

---

## 🌐 Enlaces Importantes

- **Página Web:** [Visita nuestra página](https://erikas-homemade.onrender.com/)
- **APK Móvil:** [Descarga el APK aquí](https://drive.google.com/file/d/1pJW2wZ1Mt1dEa3bIGWKED3d9OPfENEiA/view?usp=sharing)
- **Repositorio del APK:** [Código fuente del APK V1 Flutter](https://github.com/DarkKing516/Erikas_HomeMade_Flutter)

---

## 🛠️ Configuración del Entorno Virtual

Para configurar el entorno virtual y reinstalar las dependencias del proyecto, sigue estos pasos:

### 1. Crear un Nuevo Entorno Virtual

Instala `virtualenv` si no lo tienes: `pip install virtualenv `

Luego, Crea el entorno virtual:

```bash
virtualenv venv
```

### 2. Activar el Entorno Virtual

Activa el entorno virtual:

```bash
.\venv\Scripts\activate
```

### 3. Instalar Dependencias

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Ejecuta el proyecto:

```bash
python .\manage.py runserver
```


Para actualizar el archivo `requirements.txt` usa `pip freeze > requirements.txt`

---

## 🚀 Estado de la Barra de Navegación

Hemos implementado una variable local para controlar el estado de la barra de navegación. La primera vez que ingreses, la barra estará abierta. Si la cierras y navegas a otras páginas, mantendrá su estado (abierta o cerrada).

### Resetear el Estado de la Barra de Navegación

Si deseas resetear el estado de la barra, descomenta la siguiente línea en el archivo `template.js` y recarga la página:

```javascript
// localStorage.removeItem('sidebarState');
```

**Ubicación del archivo:**

`C:\Users\UwU\Documents\python_darkking\Erikas_HomeMade_Django\home\static\js\template.js`

**Recuerda:** Siempre deja esta línea comentada después de usarla.

---

## 📬 Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos:

- [Gmail](erikashomemade.bello@gmail.com)