from django.shortcuts import render
from cursos.models import Curso

# Create your views here.

from django.shortcuts import HttpResponse

def principal(request):
    cursos = Curso.objects.filter(publicado=True)
    return render(request, 'contenido/principal.html', {'cursos': cursos})

def cursos(request):
    return render(request, 'contenido/cursos.html')

def contacto(request):
    return render(request, 'contenido/contacto.html')