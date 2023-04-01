from django.contrib import admin
from django.urls import path
from BibliotecaVirtual import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('libros', views.libro, name='Libros'),
    path('alumnos', views.alumno, name='Alumnos'),
    path('docentes', views.docente, name='Docentes'),
    #path('libroFormulario', views.libroFormulario, name="LibroFormulario"),
    #path('alumnoFormulario', views.alumnoFormulario, name="AlumnoFormulario"),
    #path('docenteFormulario', views.docenteFormulario, name="DocenteFormulario"),
    path('busquedaLibro', views.busquedaLibro, name="BusquedaLibro"),
    path('buscar/', views.buscar),
    path('leerDocentes', views.leerDocentes, name='LeerDocentes'),
    path('leerAlumnos', views.leerAlumnos, name='LeerAlumnos'),
    path('leerLibros', views.leerLibros, name='LeerLibros'),
    path('eliminarDocente/<docente_nombre>/', views.eliminarDocente, name='EliminarDocente'),
    path('eliminarAlumno/<alumno_nombre>/', views.eliminarAlumno, name='EliminarAlumno'),
    path('eliminarLibro/<libro_nombre>/', views.eliminarLibro, name='EliminarLibro'),
    path('editarDocente/<docente_nombre>/', views.editarDocente, name='EditarDocente'),
    path('editarAlumno/<alumno_nombre>/', views.editarAlumno, name='EditarAlumno'),
    path('editarLibro/<libro_nombre>/', views.editarLibro, name='EditarLibro'), 

    path('libro/list/', views.LibroList.as_view(), name='List'),
    path('<int:pk>', views.LibroDetalle.as_view(), name='Detail'),
    path('nuevo', views.LibroCreacion.as_view(), name='New'),
    path('editar/<int:pk>', views.LibroUpdate.as_view(), name='Edit'),
    #path(r'^editar/(?P<pk>\d+)$', views.LibroUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>', views.LibroDelete.as_view(), name='Delete'),

    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Registro'),
    path('logout', LogoutView.as_view(template_name='BibliotecaVirtual/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
]
