# Tercera pre-entrega del curso de Python @ Coderhouse /GRIGOLATO Pablo Alejandro

Instrucciones para la instalación:
1. Clonar el repositorio en la carpeta local deseada a través de Git Bash.
2. Acceder a la carpeta del proyecto en cuestión a través de la terminal de VSC con el siguiente comando: cd ...\Tercera-pre-entrega-Grigolato
3. Ejecutar el siguiente comando para correr el servidor: python3 manage.py runserver
4. Abrir en el navegador la siguiente dirección: http://127.0.0.1:8000/BibliotecaVirtual/

Instrucciones para el uso:
El proyecto en cuestión consta de una biblioteca virtual que permite a alumnos y docentes acceder a los libros disponibles en la biblioteca física.
Los modelos existentes son: Libro, Alumno y Docente.

Rutas existentes:

BibliotecaVirtual/ - Vista de inicio con buscador de libros por código incluído. En caso de buscar un libro por código, si existe, se lo lista. Caso contrario, no aparece nada. Si no se ingresa código, se hace una advertencia en color rojo. Se puede buscar y encontrar tres libros precargados con código 1001, 1002 y 1003.

BibliotecaVirtual/libros - Vista de libros con formulario para la carga de nuevos libros en la base de datos.

BibliotecaVirtual/alumnos - Vista de alumnos con formulario para la carga de nuevos alumnos en la base de datos.

BibliotecaVirtual/docentes - Vista de docentes con formulario para la carga de nuevos docentes en la base de datos.

admin/ - Acceso al panel de administración. Se puede acceder al panel de administración como superusuario con los siguientes datos: user: pablo pass: 12345678
