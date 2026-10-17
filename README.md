# Repositorio base de Django

## Descripción

Este proyecto corresponde a la preentrega de un repositorio base utilizando Django. Su objetivo es preparar la estructura inicial de un proyecto web en Python.

## Tecnologías utilizadas

- Python
- Django
- SQLite

## Estructura del proyecto

- `manage.py`: permite ejecutar comandos de administración de Django.
- `blog_project/`: contiene la configuración principal del proyecto.
- `posts/`: aplicación Django del proyecto.
- `requirements.txt`: contiene las dependencias necesarias.
- `.gitignore`: indica qué archivos y carpetas no deben subirse al repositorio.

## Instalación y ejecución

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

6. Ejecutar el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

7. Abrir en el navegador la dirección:

   `http://127.0.0.1:8000/`

## Configuración

El proyecto está configurado para utilizar el idioma español y la zona horaria de Argentina.

## Repositorio

[GitHub - blog-django](https://github.com/mayracaporale/blog-django)
