
from django.shortcuts import render
from .models import Post


def inicio(request):
    posts = Post.objects.filter(
        estado="publicado"
    ).order_by("-fecha_creacion")

    return render(request, "posts/inicio.html", {
        "posts": posts
    })


def lista_posts(request):
    posts = Post.objects.filter(
        estado="publicado"
    ).order_by("-fecha_creacion")

    return render(request, "posts/lista_posts.html", {
        "posts": posts
    })


def acerca(request):
    return render(request, "posts/acerca.html")
