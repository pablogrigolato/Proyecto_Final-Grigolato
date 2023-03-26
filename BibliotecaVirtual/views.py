from django.shortcuts import render
from django.http import HttpResponse
from BibliotecaVirtual.models import Libro, Alumno, Docente
from BibliotecaVirtual.forms import LibroFormulario, AlumnoFormulario, DocenteFormulario

# Create your views here.

def inicio(request):
    return render(request, "BibliotecaVirtual/inicio.html")

#def libro(request):
#    return render(request, "BibliotecaVirtual/libros.html")

#def alumno(request):
#    return render(request, "BibliotecaVirtual/alumnos.html")

#def docente(request):
#    return render(request, "BibliotecaVirtual/docentes.html")

def libro(request):
    if request.method == 'POST': 
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro(nombre=request.POST['nombre'],
                      autor=request.POST['autor'],
                      codigo=request.POST['codigo']
                      )
            libro.save()
            return render(request, "BibliotecaVirtual/inicio.html")
        
    else:
        miFormulario = LibroFormulario()
            
    return render(request,"BibliotecaVirtual/libros.html", {"miFormulario": miFormulario})

def alumno(request):
    if request.method == 'POST': 
        miFormulario = AlumnoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alumno = Alumno(nombre=request.POST['nombre'],
                      apellido=request.POST['apellido'],
                      dni=request.POST['dni'],
                      email=request.POST['email']
                      )
            alumno.save()
            return render(request, "BibliotecaVirtual/inicio.html")
        
    else:
        miFormulario = AlumnoFormulario()
            
    return render(request,"BibliotecaVirtual/alumnos.html", {"miFormulario": miFormulario})

def docente(request):
    if request.method == 'POST': 
        miFormulario = DocenteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alumno = Docente(nombre=request.POST['nombre'],
                      apellido=request.POST['apellido'],
                      dni=request.POST['dni'],
                      email=request.POST['email'],
                      asignatura=request.POST['asignatura']
                      )
            alumno.save()
            return render(request, "BibliotecaVirtual/inicio.html")
        
    else:
        miFormulario = DocenteFormulario()
            
    return render(request,"BibliotecaVirtual/docentes.html", {"miFormulario": miFormulario})

def busquedaLibro(request):
    return render(request,"BibliotecaVirtual/busquedaLibro.html")

def buscar(request):
    if request.GET['codigo']:
        codigo = request.GET['codigo']
        libros = Libro.objects.filter(codigo__icontains=codigo)
        return render(request, "BibliotecaVirtual/inicio.html", {"libros":libros, "codigo":codigo})
    else:
        respuesta = "No enviaste datos."
        
    return render(request, "BibliotecaVirtual/inicio.html", {"respuesta":respuesta})
