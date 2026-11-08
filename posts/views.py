from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def inicio(request):
    posts = Post.objects.filter(
        estado="publicado"
    ).order_by("-fecha_creacion")

    return render(request, "posts/inicio.html", {
        "posts": posts
    })


def lista_posts(request):
    posts = Post.objects.all().order_by("-fecha_creacion")

    return render(request, "posts/lista_posts.html", {
        "posts": posts
    })


def acerca(request):
    return render(request, "posts/acerca.html")


# Ver detalle de un post
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, "posts/detalle_post.html", {
        "post": post
    })


# Crear un post
@login_required
def crear_post(request):
    if request.method == "POST":
        formulario = PostForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect("lista_posts")
    else:
        formulario = PostForm()

    return render(request, "posts/post_form.html", {
        "formulario": formulario
    })


# Editar un post
@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        formulario = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if formulario.is_valid():
            formulario.save()
            return redirect("detalle_post", pk=post.pk)
    else:
        formulario = PostForm(instance=post)

    return render(request, "posts/post_form.html", {
        "formulario": formulario
    })


# Eliminar un post
@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("lista_posts")

    return render(request, "posts/post_confirm_delete.html", {
        "post": post
    })