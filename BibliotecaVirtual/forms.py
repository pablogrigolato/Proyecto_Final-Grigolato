from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username = forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)
    
    class Meta:
        model = User
        fields = ['imagen']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
