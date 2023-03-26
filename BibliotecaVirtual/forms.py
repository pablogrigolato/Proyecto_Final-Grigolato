from django import forms

class LibroFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    autor = forms.CharField(max_length=40)
    codigo = forms.IntegerField()

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()

class DocenteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    email = forms.EmailField()
    asignatura = forms.CharField(max_length=40)
