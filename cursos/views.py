from django.shortcuts import render
from .models import Curso

def lista_cursos(request):
    cursos = Curso.objects.filter(publicado=True)
    return render(request, 'contenido/cursos.html', {'cursos': cursos})