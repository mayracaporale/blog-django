# Blog Django

Proyecto de blog desarrollado con Python y Django. Integra plantillas HTML, estilos CSS, publicaciones almacenadas en SQLite, gestión de imágenes, autenticación de usuarios y perfiles personalizados.

## Preentregas 8 y 9: Modelos y administración

### Funcionalidades

- Página de inicio con publicaciones dinámicas.
- Página Acerca de.
- Navegación mediante URLs de Django.
- Plantilla base `base.html` reutilizada mediante herencia.
- Estilos personalizados mediante archivos estáticos.
- Modelo `Post` para almacenar publicaciones.
- Administración de publicaciones desde Django Admin.
- Estados de publicación: Borrador, Publicado y Archivado.
- Listado de publicaciones publicadas ordenadas desde la más reciente hasta la más antigua.

### Modelo Post

El modelo `Post` incluye los siguientes campos:

- `titulo`: título de la publicación.
- `contenido`: contenido de la publicación.
- `autor`: autor de la publicación.
- `fecha_creacion`: fecha y hora de creación.
- `estado`: estado de la publicación.

El modelo implementa el método `__str__()` para mostrar el título.

### Administración

Se configuraron columnas para visualizar título, autor, estado y fecha de creación, filtros por estado y fecha, y búsqueda por título, contenido y autor.

## Preentrega 10: CRUD de publicaciones con imágenes

Se implementó un sistema CRUD para gestionar publicaciones desde la interfaz web.

### Funcionalidades

- Listar publicaciones.
- Ver el detalle de cada publicación.
- Crear publicaciones.
- Editar publicaciones existentes.
- Eliminar publicaciones con confirmación previa.
- Subir y visualizar imágenes asociadas a cada publicación.

### Manejo de imágenes

Se incorporó el campo `ImageField` al modelo `Post`, utilizando Pillow para procesar imágenes.

Se configuraron:

- `MEDIA_URL = '/media/'`
- `MEDIA_ROOT = BASE_DIR / 'media'`

Los formularios utilizan `enctype="multipart/form-data"` y las vistas procesan archivos mediante `request.FILES`.

Las imágenes de publicaciones se almacenan en `media/posts/`.

## Preentrega 11: Autenticación, usuarios y perfiles

Se incorporó un sistema de autenticación y gestión de usuarios utilizando las herramientas de Django.

### Funcionalidades

- Registro de nuevos usuarios.
- Inicio de sesión (login).
- Cierre de sesión (logout).
- Visualización del perfil del usuario.
- Edición de los datos del perfil.
- Incorporación de biografía y enlace web.
- Subida y visualización de avatar.
- Navegación condicional según el estado de autenticación.

### Modelo Perfil

Se creó el modelo `Perfil`, relacionado con el modelo `User` de Django mediante `OneToOneField`.

Incluye los siguientes campos:

- `user`: relación uno a uno con el usuario.
- `biografia`: descripción personal.
- `link_web`: enlace a un sitio web.
- `avatar`: imagen de perfil.

El perfil se crea desde la vista de registro mediante la creación explícita de una instancia asociada al usuario.

### Formularios

Se implementaron formularios utilizando:

- `UserCreationForm` para el registro de usuarios.
- `ModelForm` para la edición del perfil.

### Protección de vistas

Se utilizó el decorador `@login_required` para restringir el acceso a las siguientes funcionalidades:

- Crear publicaciones.
- Editar publicaciones.
- Eliminar publicaciones.

Las páginas públicas del blog continúan disponibles para los visitantes.

### Administración de perfiles

El modelo `Perfil` se registró en Django Admin para permitir visualizar y administrar los perfiles de los usuarios.

## Estructura del proyecto

- `posts/models.py`: modelo de publicaciones.
- `posts/admin.py`: configuración del administrador de publicaciones.
- `posts/views.py`: vistas y consultas mediante el ORM.
- `posts/urls.py`: rutas de publicaciones.
- `posts/forms.py`: formulario de publicaciones.
- `posts/templates/posts/`: plantillas HTML del blog.
- `posts/static/posts/css/estilos.css`: estilos visuales.
- `accounts/models.py`: modelo de perfil.
- `accounts/forms.py`: formularios de registro y perfil.
- `accounts/views.py`: vistas de registro y gestión de perfiles.
- `accounts/urls.py`: rutas de autenticación y perfiles.
- `accounts/admin.py`: configuración del administrador de perfiles.
- `blog_project/settings.py`: configuración general del proyecto.
- `blog_project/urls.py`: rutas principales del proyecto.

## Instalación y ejecución

### Requisitos

- Python instalado.
- Git instalado.

### Pasos para ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/mayracaporale/blog-django.git
```

2. Ingresar a la carpeta:

```bash
cd blog-django
```

3. Crear un entorno virtual:

```bash
python -m venv venv
```

4. Activar el entorno virtual en Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

5. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

6. Aplicar las migraciones:

```bash
python manage.py migrate
```

7. Crear un superusuario para acceder al panel administrativo:

```bash
python manage.py createsuperuser
```

8. Iniciar el servidor:

```bash
python manage.py runserver
```

9. Abrir el sitio en el navegador:

http://127.0.0.1:8000/

## Panel de administración

Para acceder al administrador de Django:

http://127.0.0.1:8000/admin/

Ingresar con las credenciales del superusuario creado anteriormente.

Desde el panel se pueden administrar publicaciones y perfiles de usuarios.

## Pruebas realizadas

- Comprobación de la configuración mediante `python manage.py check`.
- Generación y aplicación de migraciones.
- Creación y administración de publicaciones.
- Verificación de publicaciones con distintos estados.
- Comprobación del listado y detalle de publicaciones.
- Pruebas de creación, edición y eliminación de publicaciones.
- Verificación de subida y visualización de imágenes.
- Registro de nuevos usuarios.
- Pruebas de inicio y cierre de sesión.
- Visualización y edición del perfil.
- Verificación de subida y visualización del avatar.
- Comprobación de acceso restringido a las vistas de creación, edición y eliminación de publicaciones.
- Verificación del acceso al panel de administración.

## Tecnologías utilizadas

Python · Django · SQLite · HTML · CSS · Pillow · Git · GitHub

## Repositorio

[GitHub - Blog Django](https://github.com/mayracaporale/blog-django)