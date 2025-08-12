from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'contenido'  # Namespace para la app

urlpatterns = [
    path('', views.principal, name='principal'),  # Ruta para la página principal
    path('cursos/', views.cursos, name='cursos'),  # Página pública de cursos
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)