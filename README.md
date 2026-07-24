# Mi Blog — Proyecto final (Django)

Aplicación web de blog desarrollada con Django, que permite crear, editar,
eliminar y buscar entradas por autor, con registro de usuarios, gestión de
perfil y panel de administración.

## Descripción del proyecto

El propósito de este proyecto es implementar una aplicación de blog completa
respetando la arquitectura **MVT (Model-View-Template)** de Django y el
patrón **CRUD** sobre las entradas del blog. Resuelve la necesidad de que
distintos usuarios puedan publicar y gestionar su propio contenido de forma
independiente, con control de permisos (cada usuario solo puede editar o
eliminar sus propios posts) y un panel de administración centralizado para
la gestión general de contenido y usuarios.

Está orientada a cualquier persona que quiera llevar un blog personal o
colaborativo: cada usuario registrado puede publicar sus propias entradas,
gestionar su perfil y navegar/buscar el contenido de otros autores.

## Funcionalidades principales

- **Panel de administración de Django** (`/admin/`): gestión completa de
  entradas (`Post`) y de usuarios (crear, editar, activar/desactivar,
  asignar permisos).
- **Registro de usuarios**, con validación de email duplicado.
- **Inicio de sesión**, con aviso explícito y link a registro cuando el
  usuario ingresado no existe.
- **Cierre de sesión.**
- **Gestión de perfil**: cada usuario puede ver sus datos y sus propios
  posts, editar su nombre de usuario/email, y cambiar su contraseña.
- **CRUD completo de entradas de blog**: crear, ver, editar y eliminar
  posts, con permisos (solo el autor puede editar/eliminar los suyos).
- **Búsqueda de entradas por autor.**
- **Formularios con validación** de datos en servidor (longitud mínima de
  título/contenido, email no duplicado).
- **Navegación** entre todas las pantallas mediante un menú común.

## Tecnologías

Python, Django, SQLite3 (desarrollo), Git/GitHub, Gunicorn y Whitenoise
(producción), desplegado en Render.

## Pasos para ejecutar localmente

Requisitos previos: Python 3.10+ y Git instalados.

```bash
# 1. Clonar el repositorio
git clone https://github.com/IsmaOstk/MiBlog-Django.git
cd MiBlog-Django

# 2. Crear y activar el entorno virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear un superusuario (para acceder al panel /admin/)
python manage.py createsuperuser

# 6. Levantar el servidor de desarrollo
python manage.py runserver
```

Abrí `http://127.0.0.1:8000/` en el navegador. El panel de administración
queda disponible en `http://127.0.0.1:8000/admin/`.

## URL pública

**https://miblog-django.onrender.com**

## Despliegue

Desplegado en **Render** (plan gratuito), usando **Gunicorn** como servidor
WSGI y **Whitenoise** para servir los archivos estáticos. La configuración
sensible (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`) se maneja mediante
variables de entorno del servicio, nunca hardcodeada en el repositorio.

- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start Command**: `gunicorn miblog.wsgi:application`

## Evidencia visual del funcionamiento

https://docs.google.com/presentation/d/1PQE7lxNhoewzjMzS6M2kjqsXULGCWiHEbNu_KPq4dYo/edit?usp=sharing

### Panel de administración

### Registro de usuario

### Login — aviso de usuario inexistente


### Listado de posts y búsqueda por autor
_

### Detalle de un post


### Crear / editar un post


### Perfil de usuario


### Edición de perfil y cambio de contraseña

