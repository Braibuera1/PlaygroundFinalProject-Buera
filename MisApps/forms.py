from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Pelicula, Serie, Libro, Comentario, ComentarioSerie, ComentarioLibro


class UserRegisterFormCustom(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username')  

              
class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                    widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')     
        
         
        
class PeliculaFormulario(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'director', 'genero', 'sinopsis', 'imagen'] 
    
class SerieFormulario(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['titulo', 'plataforma', 'genero', 'sinopsis', 'imagen'] 
        
class LibroFormulario(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'genero', 'sinopsis', 'imagen']      
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']

class ComentarioFormSerie(forms.ModelForm):
    class Meta:
        model = ComentarioSerie
        fields = ['contenido']    
        
class ComentarioFormLibro(forms.ModelForm):
    class Meta:
        model = ComentarioLibro
        fields = ['contenido']                           
            
        

        

    
