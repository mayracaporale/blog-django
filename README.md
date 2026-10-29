# Blog Django

## Preentrega 8: Sitio web con Django

El proyecto implementa una primera versión visual de un blog utilizando Django, HTML y CSS.

### Funcionalidades

- Página de inicio con mensaje de bienvenida y publicaciones.
- Página Acerca de con información sobre la autora y el propósito del sitio.
- Navegación entre páginas mediante URLs de Django.
- Plantilla base `base.html` reutilizada mediante herencia.
- Estilos personalizados cargados desde archivos estáticos.

### Estructura visual

- `posts/templates/posts/base.html`: estructura general y navegación.
- `posts/templates/posts/inicio.html`: página principal.
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

7. Iniciar el servidor:

   ```bash
   python manage.py runserver
   ```

8. Abrir el sitio en el navegador:

   http://127.0.0.1:8000/

### Panel de administración

Para acceder al administrador de Django, ingresar a:

http://127.0.0.1:8000/admin/

Si todavía no existe un superusuario, crearlo con:

```bash
python manage.py createsuperuser
```

## Configuración

El proyecto está configurado para utilizar el idioma español y la zona horaria de Argentina.

## Preentrega 9: Modelos y Admin configurados

### Descripción

En esta etapa se configuró el modelo `Post` de Django y su administración desde el panel de administración.

### Modelo Post

El modelo incluye los siguientes campos:

- `titulo`: título de la publicación.
- `contenido`: contenido de la publicación.
- `autor`: autor de la publicación.
- `fecha_creacion`: fecha y hora de creación generadas automáticamente.
- `estado`: estado de la publicación, con las opciones Borrador, Publicado y Archivado.

También se implementó el método `__str__()` para mostrar el título de cada publicación.

### Panel de administración

Se registró el modelo `Post` en Django Admin y se configuraron:

- Columnas para visualizar título, autor, estado y fecha de creación.
- Filtros por estado y fecha de creación.
- Búsqueda por título, contenido y autor.

### Listado de publicaciones

Se configuró el listado para mostrar únicamente publicaciones con estado `publicado`, ordenadas desde la más reciente hasta la más antigua.

### Pruebas realizadas

- Migraciones aplicadas correctamente.
- Modelo disponible en el administrador de Django.
- Creación de tres publicaciones de prueba.
-Verificación de las publicaciones en la página Publicaciones del blog (/posts/)

### Tecnologías

Python · Django · SQLite · HTML · CSS

## Repositorio

[GitHub - blog-django](https://github.com/mayracaporale/blog-django)
