from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }



#formulario para aregar cursos

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'nivel': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
        labels = {
            'clave': 'Código del curso',
            'publicado': '¿Publicar este curso?',
        }