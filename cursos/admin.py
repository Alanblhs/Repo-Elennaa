# cursos/admin.py
from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre', 'nivel', 'categoria', 'publicado', 'fecha_creacion')
    list_filter = ('publicado', 'categoria', 'nivel')
    search_fields = ('nombre', 'descripcion', 'clave')
    date_hierarchy = 'fecha_creacion'
    ordering = ['fecha_creacion']
    fieldsets = (
        ("Información general", {'fields': ('clave', 'nombre', 'descripcion', 'nivel', 'categoria', 'publicado')}),
        ("Multimedia y metadatos", {'fields': ('portada', 'fecha_creacion'),'classes': ('collapse',)}),
    )
    readonly_fields = ('fecha_creacion',)




    class CursoAdmin(admin.ModelAdmin):
        list_display = ('clave', 'nombre', 'nivel', 'categoria', 'publicado', 'fecha_creacion')
        list_filter = ('publicado', 'categoria', 'nivel')
        search_fields = ('nombre', 'descripcion', 'clave')
        date_hierarchy = 'fecha_creacion'
        ordering = ['fecha_creacion']
        fieldsets = (
        ("Información general", {'fields': ('clave', 'nombre', 'descripcion', 'nivel', 'categoria', 'publicado')}),
        ("Multimedia y metadatos", {'fields': ('portada', 'fecha_creacion'),'classes': ('collapse',)}),
    )
    readonly_fields = ('fecha_creacion',)