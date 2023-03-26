from django.contrib import admin
from django.urls import path
from BibliotecaVirtual import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('libros', views.libro, name='Libros'),
    path('alumnos', views.alumno, name='Alumnos'),
    path('docentes', views.docente, name='Docentes'),
    #path('libroFormulario', views.libroFormulario, name="LibroFormulario"),
    #path('alumnoFormulario', views.alumnoFormulario, name="AlumnoFormulario"),
    #path('docenteFormulario', views.docenteFormulario, name="DocenteFormulario"),
    path('busquedaLibro', views.busquedaLibro, name="BusquedaLibro"),
    path('buscar', views.buscar),
]
