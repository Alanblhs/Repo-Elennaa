from django.shortcuts import render
from cursos.models import Curso

def principal(request):
    cursos = Curso.objects.filter(publicado=True).order_by('-fecha_creacion')[:5]
    return render(request, 'contenido/principal.html', {'cursos': cursos})

def cursos(request):
    return render(request, 'contenido/cursos.html')

def contacto(request):
    return render(request, 'contenido/contacto.html')