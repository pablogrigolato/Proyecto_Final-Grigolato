from django.shortcuts import render
from django.http import HttpResponse
from BibliotecaVirtual.models import Libro, Alumno, Docente, Avatar
from BibliotecaVirtual.forms import LibroFormulario, AlumnoFormulario, DocenteFormulario, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
from BibliotecaVirtual.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
#from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#def inicio(request):
#    return render(request, "BibliotecaVirtual/inicio.html")

#def libro(request):
#    return render(request, "BibliotecaVirtual/libros.html")

#def alumno(request):
#    return render(request, "BibliotecaVirtual/alumnos.html")

#def docente(request):
#    return render(request, "BibliotecaVirtual/docentes.html")

def libro(request):
    if request.method == 'POST': 
        miFormulario = LibroFormulario(request.POST, request.FILES)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro(nombre=request.POST['nombre'],
                      autor=request.POST['autor'],
                      codigo=request.POST['codigo'],
                      tapa=informacion['tapa'],
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
            docente = Docente(nombre=request.POST['nombre'],
                      apellido=request.POST['apellido'],
                      dni=request.POST['dni'],
                      email=request.POST['email'],
                      asignatura=request.POST['asignatura']
                      )
            docente.save()
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

def leerDocentes(request):
    docentes = Docente.objects.all()
    contexto = {"docentes": docentes}
    return render(request, "BibliotecaVirtual/leerDocentes.html", contexto)

def leerAlumnos(request):
    alumnos = Alumno.objects.all()
    contexto = {"alumnos": alumnos}
    return render(request, "BibliotecaVirtual/leerAlumnos.html", contexto)

def leerLibros(request):
    libros = Libro.objects.all()
    contexto = {"libros": libros}
    return render(request, "BibliotecaVirtual/leerLibros.html", contexto)

def eliminarDocente(request, docente_nombre):
    docente = Docente.objects.get(nombre=docente_nombre)
    docente.delete()
    docentes = Docente.objects.all()
    contexto = {"docentes": docentes}
    return render(request, "BibliotecaVirtual/leerDocentes.html", contexto)

def eliminarAlumno(request, alumno_nombre):
    alumno = Alumno.objects.get(nombre=alumno_nombre)
    alumno.delete()
    alumnos = Alumno.objects.all()
    contexto = {"alumnos": alumnos}
    return render(request, "BibliotecaVirtual/leerAlumnos.html", contexto)

def eliminarLibro(request, libro_nombre):
    libro = Libro.objects.get(nombre=libro_nombre)
    libro.delete()
    libros = Libro.objects.all()
    contexto = {"libros": libros}
    return render(request, "BibliotecaVirtual/leerLibros.html", contexto)

def editarDocente(request, docente_nombre):
    docente = Docente.objects.get(nombre=docente_nombre)
    if request.method == 'POST':
        miFormulario = DocenteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            docente.nombre = informacion['nombre']
            docente.apellido = informacion['apellido']
            docente.dni = informacion['dni']
            docente.email = informacion['email']
            docente.asignatura = informacion['asignatura']
            docente.save()
            return render(request, "BibliotecaVirtual/inicio.html")
    else:
        miFormulario = DocenteFormulario(initial={'nombre':docente.nombre,
                                                  'apellido':docente.apellido,
                                                  'dni':docente.dni,
                                                  'email':docente.email,
                                                  'asignatura':docente.asignatura})
        return render(request, "BibliotecaVirtual/editarDocente.html", {"miFormulario":miFormulario, "docente_nombre":docente_nombre})

def editarAlumno(request, alumno_nombre):
    alumno = Alumno.objects.get(nombre=alumno_nombre)
    if request.method == 'POST':
        miFormulario = AlumnoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alumno.nombre = informacion['nombre']
            alumno.apellido = informacion['apellido']
            alumno.dni = informacion['dni']
            alumno.email = informacion['email']
            alumno.save()
            return render(request, "BibliotecaVirtual/inicio.html")
    else:
        miFormulario = AlumnoFormulario(initial={'nombre':alumno.nombre,
                                                  'apellido':alumno.apellido,
                                                  'dni':alumno.dni,
                                                  'email':alumno.email})
        return render(request, "BibliotecaVirtual/editarAlumno.html", {"miFormulario":miFormulario, "alumno_nombre":alumno_nombre})

def editarLibro(request, libro_nombre):
    libro = Libro.objects.get(nombre=libro_nombre)
    if request.method == 'POST':
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro.nombre = informacion['nombre']
            libro.autor = informacion['autor']
            libro.codigo = informacion['codigo']
            libro.save()
            return render(request, "BibliotecaVirtual/inicio.html")
    else:
        miFormulario = LibroFormulario(initial={'nombre':libro.nombre,
                                                  'autor':libro.autor,
                                                  'codigo':libro.codigo})
        return render(request, "BibliotecaVirtual/editarLibro.html", {"miFormulario":miFormulario, "libro_nombre":libro_nombre})

class LibroList(ListView):
    model = Libro
    template_name = "BibliotecaVirtual/libros_list.html"

#class AlumnoList(ListView):
#    model = Alumno
#    template_name = "BibliotecaVirtual/alumnos_list.html"
#
#class DocenteList(ListView):
#    model = Docente
#    template_name = "BibliotecaVirtual/docentes_list.html"

class LibroDetalle(DetailView):
    model = Libro
    template_name = "BibliotecaVirtual/libro_detalle.html"

#class AlumnoDetalle(DetailView):
#    model = Alumno
#    template_name = "BibliotecaVirtual/alumno_detalle.html"
#
#class DocenteDetalle(DetailView):
#    model = Docente
#    template_name = "BibliotecaVirtual/docente_detalle.html"

class LibroCreacion(CreateView):
    model = Libro
    template_name = "BibliotecaVirtual/libro_form.html"
    success_url = "/BibliotecaVirtual/libro/list"
    fields = ['nombre', 'autor', 'codigo']

#class AlumnoCreacion(CreateView):
#    model = Alumno
#    template_name = "BibliotecaVirtual/alumnos_form.html"
#    success_url = reverse_lazy("BibliotecaVirtual:List")
#    fields = ['nombre', 'apellido', 'dni']
#
#class DocenteCreacion(CreateView):
#    model = Docente
#    template_name = "BibliotecaVirtual/docentes_form.html"
#    success_url = reverse_lazy("BibliotecaVirtual:List")
#    fields = ['nombre', 'apellido', 'dni']

class LibroUpdate(UpdateView):
    model = Libro
    success_url = "/BibliotecaVirtual/libro/list"
    template_name = "BibliotecaVirtual/libro_form.html"
    fields = ['nombre', 'autor', 'codigo']

#class AlumnoUpdate(UpdateView):
#    model = Alumno
#    success_url = "/BibliotecaVirtual/alumno/list"
#    template_name = "alumnos_form.html"
#    fields = ['nombre', 'apellido', 'dni']
#
#class DocenteUpdate(UpdateView):
#    model = Docente
#    success_url = "/BibliotecaVirtual/docente/list"
#    template_name = "docentes_form.html"
#    fields = ['nombre', 'apellido', 'dni']

class LibroDelete(DeleteView):
    model = Libro
    template_name = "BibliotecaVirtual/libro_confirm_delete.html"
    success_url = "/BibliotecaVirtual/libro/list"

#class AlumnoDelete(DeleteView):
#    model = Alumno
#    template_name = "BibliotecaVirtual/alumno_confirm_delete.html"
#    success_url = "/BibliotecaVirtual/alumno/list"
#
#class DocenteDelete(DeleteView):
#    model = Docente
#    template_name = "BibliotecaVirtual/docente_confirm_delete.html"
#    success_url = "/BibliotecaVirtual/docente/list"


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data =request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contras)
            if user is not None:
                login(request, user)
                return render(request,"BibliotecaVirtual/inicio.html", {"mensaje":f"Bienvenido {usuario}."})
            else:
                return render(request,"BibliotecaVirtual/inicio.html", {"mensaje":"Error por datos incorrectos."})
        else:
            return render(request, "BibliotecaVirtual/inicio.html", {"mensaje":"Error por formulario erróneo."})
    form = AuthenticationForm()
    return render(request,"BibliotecaVirtual/login.html", {"form":form})

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'BibliotecaVirtual/inicio.html', {'mensaje':'Usuario creado :)'})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'BibliotecaVirtual/registro.html', {'form':form})

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(render, 'BibliotecaVirtual/inicio.html', {'url':avatares[0].imagen.url})

#class CLaseQueNecesitaLogin(LoginRequiredMixin)

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(miFormulario)
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'BibliotecaVirtual/inicio.html', {'mensaje':'Contraseña incorrecta.'})
            return render(request, 'BibliotecaVirtual/inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "BibliotecaVirtual/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'BibliotecaVirtual/inicio.html')
    else:
        miFormulario = AvatarFormulario()
    return render(request, "BibliotecaVirtual/agregarAvatar.html", {"miFormulario":miFormulario})
