# Proyecto Final del curso de Python @ Coderhouse /GRIGOLATO Pablo Alejandro

Instrucciones para la instalación:
1. Clonar el repositorio en la carpeta local deseada a través de Git Bash.
2. Acceder a la carpeta del proyecto en cuestión a través de la terminal de VSC con el siguiente comando: cd ...\Tercera-pre-entrega-Grigolato
3. Ejecutar el siguiente comando para correr el servidor: python3 manage.py runserver
4. Abrir en el navegador la siguiente dirección: http://127.0.0.1:8000/BibliotecaVirtual/

Instrucciones para el uso:
El proyecto en cuestión consta de una biblioteca virtual que permite a alumnos y docentes acceder a los libros disponibles en la biblioteca física.
Los modelos existentes son: Libro, Alumno, Docente y Avatar.

Rutas existentes:

admin/ - Acceso al panel de administración. Se puede acceder al panel de administración como superusuario con los siguientes datos: user: pablo pass: 12345678

BibliotecaVirtual/ - Vista de inicio con buscador de libros por código incluído. En caso de buscar un libro por código, si existe, se lo lista. Caso contrario, no aparece nada. Si no se ingresa código, se hace una advertencia en color rojo. Se puede buscar y encontrar libros precargados por código.

BibliotecaVirtual/libros - Vista de libros con formulario para la carga de nuevos libros en la base de datos.

BibliotecaVirtual/alumnos - Vista de alumnos con formulario para la carga de nuevos alumnos en la base de datos.

BibliotecaVirtual/docentes - Vista de docentes con formulario para la carga de nuevos docentes en la base de datos.

BibliotecaVirtual/busquedaLibro - Vista para la búsqueda de libros por código.

BibliotecaVirtual/leerDocentes - Vista para listar docentes en base de datos con la posibilidad de acceder a las vistas listadas a continuación para editar y eliminar registros.

BibliotecaVirtual/eliminarDocente/<docente_nombre>/ - Eliminar docente
BibliotecaVirtual/editarDocente/<docente_nombre>/ - Editar docente

BibliotecaVirtual/leerAlumnos - Vista para listar alumnos en base de datos con la posibilidad de acceder a las vistas listadas a continuación para editar y eliminar registros.

BibliotecaVirtual/eliminarAlumno/<alumno_nombre>/ - Eliminar alumno
BibliotecaVirtual/editarAlumno/<alumno_nombre>/ - Editar alumno

BibliotecaVirtual/leerLibros - Vista para listar libros en base de datos con la posibilidad de acceder a las vistas listadas a continuación para editar y eliminar registros.

BibliotecaVirtual/eliminarLibro/<libro_nombre>/ - Eliminar libro
BibliotecaVirtual/editarLibro/<libro_nombre>/ - Editar libro

BibliotecaVirtual/libro/list/ - Vista para el listado de libros con la posibilidad de acceder a las vistas listadas a continuación para crear, editar y eliminar registros.

BibliotecaVirtual/<int:pk> - Detail
BibliotecaVirtual/nuevo - New
BibliotecaVirtual/editar/<int:pk> - Edit
BibliotecaVirtual/borrar/<int:pk> - Delete

BibliotecaVirtual/login - Vista simple de ingreso de usuarios para destrabar funcionalidades del sitio.

BibliotecaVirtual/register - Vista para el registro de nuevos usuarios.

BibliotecaVirtual/logout - Vista para desvincular a un usuario del sitio.

BibliotecaVirtual/editarPerfil - Vista para la edición de algún campo de cada usuario.

BibliotecaVirtual/agregarAvatar - Vista para agregar un Avatar al usuario.

About/ - Segunda aplicación con vista del inicio sin accesos a herramientas disponibles únicamente para personas con usuarios, con descripción breve de la BibliotecaVirtual.





Test realizados
Para ver los tests realizados abrir el archivo "Casos de prueba.xlsx"


Video demo de funcionamiento del sitio
https://drive.google.com/file
