from django.shortcuts import render


from django.shortcuts import render
from .models import Publicacion


def inicio(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    return render(request, 'posts/inicio.html', {
        'publicaciones': publicaciones
    })

