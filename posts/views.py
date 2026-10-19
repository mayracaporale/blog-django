
from django.shortcuts import render
from .models import Publicacion


def inicio(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    return render(request, 'posts/inicio.html', {
        'publicaciones': publicaciones
    })


def acerca(request):
    return render(request, 'posts/acerca.html')
