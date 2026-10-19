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

### Ejecutar el proyecto

Desde la carpeta donde se encuentra `manage.py`, ejecutar:

```bash
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` en el navegador.
