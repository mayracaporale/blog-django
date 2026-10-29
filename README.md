# Blog Django

Proyecto de blog desarrollado con Python y Django, que integra páginas web con plantillas HTML, estilos CSS y publicaciones almacenadas en una base de datos SQLite.

## Preentrega 8 y Preentrega 9

### Funcionalidades

- Página de inicio con mensaje de bienvenida y publicaciones dinámicas.
- Página Acerca de con información sobre la autora y el propósito del sitio.
- Navegación entre páginas mediante URLs de Django.
- Plantilla base `base.html` reutilizada mediante herencia.
- Estilos personalizados cargados desde archivos estáticos.
- Modelo `Post` para almacenar publicaciones en la base de datos.
- Administración de publicaciones desde el panel de Django.
- Estados de publicación: Borrador, Publicado y Archivado.
- Listado de publicaciones publicadas ordenadas desde la más reciente hasta la más antigua.

### Estructura del proyecto

- `posts/models.py`: definición del modelo `Post`.
- `posts/admin.py`: registro y configuración del panel de administración.
- `posts/views.py`: vistas y consultas mediante el ORM de Django.
- `posts/urls.py`: rutas de la aplicación.
- `posts/templates/posts/base.html`: estructura general y navegación.
- `posts/templates/posts/inicio.html`: página principal.
- `posts/templates/posts/lista_posts.html`: listado de publicaciones.
- `posts/templates/posts/acerca.html`: información sobre el blog.
- `posts/static/posts/css/estilos.css`: estilos visuales.

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

### Panel de administración

Para acceder al administrador de Django, ingresar a:

http://127.0.0.1:8000/admin/

Iniciar sesión con las credenciales del superusuario creado anteriormente. Desde el panel se pueden crear, editar y administrar publicaciones.

## Modelo Post

El modelo `Post` incluye los siguientes campos:

- `titulo`: título de la publicación.
- `contenido`: contenido de la publicación.
- `autor`: autor de la publicación.
- `fecha_creacion`: fecha y hora de creación generadas automáticamente.
- `estado`: estado de la publicación, con las opciones Borrador, Publicado y Archivado.

El modelo implementa el método `__str__()` para mostrar el título de cada publicación.

## Panel de administración

El modelo `Post` está registrado en Django Admin. Se configuraron:

- Columnas para visualizar título, autor, estado y fecha de creación.
- Filtros por estado y fecha de creación.
- Búsqueda por título, contenido y autor.

## Listado de publicaciones

Las vistas consultan los posts almacenados en SQLite mediante el ORM de Django.

El listado de publicaciones muestra únicamente los posts cuyo estado es `publicado`, ordenados por fecha de creación descendente.

Las plantillas utilizan el bucle `{% for post in posts %}` para mostrar dinámicamente el título, contenido, autor y fecha de cada publicación.

## Pruebas realizadas

- Comprobación de la configuración del proyecto mediante `python manage.py check`.
- Migraciones generadas y aplicadas.
- Modelo disponible y editable desde el panel de administración.
- Creación de tres publicaciones con estados diferentes.
- Verificación del listado de publicaciones en `/posts/`.
- Verificación de la visualización dinámica de publicaciones publicadas en la página de inicio.

## Tecnologías

Python · Django · SQLite · HTML · CSS · Git · GitHub

## Repositorio

[GitHub - blog-django](https://github.com/mayracaporale/blog-django)
