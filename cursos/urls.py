from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.lista_cursos, name='lista'),
    path('nuevo/', views.crear_curso, name='crear'),
    path('<int:pk>/', views.detalle_curso, name='detalle'),
    path('<int:pk>/editar/', views.editar_curso, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_curso, name='eliminar'),
]



app_name = 'cursos'

urlpatterns = [
    path('admin_cursos/', views.lista_cursos, name='lista'),
    path('admin_cursos/nuevo/', views.crear_curso, name='crear'),
    path('admin_cursos/<int:pk>/editar/', views.editar_curso, name='editar'),  # Esta es la línea clave
    path('admin_cursos/<int:pk>/eliminar/', views.eliminar_curso, name='eliminar'),
    path('admin_cursos/<int:pk>/confirmar-eliminar/', views.confirmar_eliminar_curso, name='confirmar_eliminar'),

    
]