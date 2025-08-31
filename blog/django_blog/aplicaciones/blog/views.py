from django.shortcuts import render
from django.templatetags.static import static
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    posts = Post.objects.filter(estado = True)

    context = {
        'posts':posts,
        'imagen_url': static('assets/img/home-bg.jpg')
    }
    return render(request,'index.html', context)

def detallePost(request, slug):
    post = get_object_or_404(Post,slug = slug)
    #post = Post.objects.get(slug = slug)

    context = {
        'post':post,
        'imagen_url': post.imagen
    }
    return render(request, 'post.html', context)
    

def programacion(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = "Programación")
    )

    context = {
        'posts': posts,
        'imagen_url': static('assets/img/programacion.jpg')
    }
    return render(request, 'programacion.html', context)

def generales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = "General")
    )
    context = {
        'posts':posts,
        'imagen_url': static('assets/img/post-bg.jpg')
    }
    return render(request, 'generales.html', context)

def videojuegos(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = "Videojuegos")
    )
    context = {
        'posts':posts,
        'imagen_url': static('assets/img/videojuegos.jpg')
    }
    return render(request, 'videojuegos.html', context)

def tecnologia(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = "Tecnología")
    )
    context = {
        'posts':posts,
        'imagen_url': static('assets/img/tecnologia.jpg')
    }
    return render(request, 'tecnologia.html', context)

def tutoriales(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = "Tutoriales")
    )
    context = {
        'posts':posts,
        'imagen_url': static('assets/img/tutoriales.jpg')
    }
    return render(request, 'tutoriales.html', context)
