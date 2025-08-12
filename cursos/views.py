'''from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Curso
from .forms import CursoForm


def lista_cursos(request):
    cursos = Curso.objects.filter(publicado=True)
    return render(request, 'contenido/cursos.html', {'cursos': cursos})'''




from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm
from django.contrib import messages



def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos:lista')
    else:
        form = CursoForm()
    return render(request, 'cursos/curso_form.html', {'form': form})

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/curso_detalle.html', {'curso': curso})

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:detalle', pk=curso.pk)
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/curso_form.html', {'form': form})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos:lista')
    return render(request, 'cursos/curso_confirmar_eliminar.html', {'curso': curso})



#creacion del curso
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos:lista')  # Redirige a la lista después de guardar
    else:
        form = CursoForm()
    
    return render(request, 'cursos/curso_form.html', {
        'form': form,
        'titulo': 'Nuevo Curso'
    })



#edicion del curos

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:lista')
    else:
        form = CursoForm(instance=curso)
    
    return render(request, 'cursos/curso_form.html', {
        'form': form,
        'titulo': f'Editar Curso: {curso.nombre}'
    })


#eliminar curso




def confirmar_eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/confirmar_eliminar.html', {'curso': curso})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, f'El curso "{curso.nombre}" ha sido eliminado correctamente.')
        return redirect('cursos:lista')
    return redirect('cursos:confirmar_eliminar', pk=pk)