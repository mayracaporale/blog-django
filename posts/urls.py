from django.urls import path
from . import views

urlpatterns = [
    # Inicio
    path("", views.inicio, name="inicio"),

    # Listado de publicaciones
    path("posts/", views.lista_posts, name="lista_posts"),

    # Detalle de una publicación
    path("posts/<int:pk>/", views.detalle_post, name="detalle_post"),

    # Crear publicación
    path("posts/crear/", views.crear_post, name="crear_post"),

    # Editar publicación
    path("posts/<int:pk>/editar/", views.editar_post, name="editar_post"),

    # Eliminar publicación
    path("posts/<int:pk>/eliminar/", views.eliminar_post, name="eliminar_post"),

    # Acerca
    path("acerca/", views.acerca, name="acerca"),
]