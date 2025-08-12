from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contenido.urls')),  # Incluye las URLs de contenido
    path('admin_cursos/', include('cursos.urls')),  # URLs para administración de cursos
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)