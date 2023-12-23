from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import ComentarioForm,ComentarioFormSerie, ComentarioFormLibro, UserRegisterFormCustom, PeliculaFormulario, FormularioEdicion, FormularioCambioPassword, SerieFormulario, LibroFormulario
from .models import Pelicula, Serie, Libro, Comentario, ComentarioSerie, ComentarioLibro
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import  UpdateView
from django.views.generic import  ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin





def inicio(request):
    return render(request,'base.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterFormCustom(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"index.html",{'mensaje':"Usuario Creado"})
    else:
        form = UserRegisterFormCustom()
    return render(request,"register.html",{'form':form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():  # Si la validación de Django es exitosa
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "index.html", {"mensaje": f'Bienvenido {user.username}'})
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionuser.html'
    success_url = reverse_lazy('pagina principal')

    def get_object(self):
        return self.request.user
    

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'Cambiar_contraseña.html'
    success_url = reverse_lazy('cambio_exitoso')

def password_exitoso(request):
    return render(request, 'nueva_contraseña.html', {})



#-----------------------------LISTA-------------------------------------------------------

class PeliculaLista(LoginRequiredMixin, ListView):
    model = Pelicula
    template_name = 'listaPeliculas.html'
    context_object_name = 'peliculas'
    login_url = 'Login'
    
class SerieLista(LoginRequiredMixin, ListView):
    model = Serie
    template_name = 'listaSeries.html'
    context_object_name = 'series'
    login_url = 'Login'
    
class LibroLista(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'listaLibros.html'
    context_object_name = 'libros'
    login_url = 'Login'      
    
    
#------------------AGREGANDO-----------------------
    
def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaFormulario(request.POST, request.FILES)
        if form.is_valid():
            nueva_pelicula = form.save(commit=False)
            nueva_pelicula.usuario = request.user 
            nueva_pelicula.save()
            return redirect('lista_peliculas')  
    else:
        form = PeliculaFormulario()

    return render(request, 'agregar_pelicula.html', {'form': form})      

def agregar_serie(request):
    if request.method == 'POST':
        form = SerieFormulario(request.POST, request.FILES)
        if form.is_valid():
            nueva_serie = form.save(commit=False)
            nueva_serie.usuario = request.user  
            nueva_serie.save()
            return redirect('lista_series')  
    else:
        form = SerieFormulario()

    return render(request, 'agregar_serie.html', {'form': form})   

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroFormulario(request.POST, request.FILES)
        if form.is_valid():
            nueva_libro = form.save(commit=False)
            nueva_libro.usuario = request.user  
            nueva_libro.save()
            return redirect('lista_libros')  
    else:
        form = LibroFormulario()

    return render(request, 'agregar_libro.html', {'form': form})  


#----------------------MOSTRAR --------------------------



def detalle_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, pk=pelicula_id)
    comentarios = Comentario.objects.filter(pelicula=pelicula)
    comentario_form = ComentarioForm()

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            nuevo_comentario = comentario_form.save(commit=False)
            nuevo_comentario.usuario = request.user
            nuevo_comentario.pelicula = pelicula
            nuevo_comentario.save()
            messages.success(request, 'Comentario agregado con éxito.')
            return redirect('detalle_pelicula', pelicula_id=pelicula.id)

    return render(request, 'detalle_pelicula.html', {'pelicula': pelicula, 'comentarios': comentarios, 'comentario_form': comentario_form})
    

def detalle_serie(request, serie_id):
    serie = get_object_or_404(Serie, pk=serie_id)
    comentarios = ComentarioSerie.objects.filter(serie=serie)
    comentario_form = ComentarioFormSerie()

    if request.method == 'POST':
        comentario_form = ComentarioFormSerie(request.POST)
        if comentario_form.is_valid():
            nuevo_comentario = comentario_form.save(commit=False)
            nuevo_comentario.usuario = request.user
            nuevo_comentario.serie = serie
            nuevo_comentario.save()
            messages.success(request, 'Comentario agregado con éxito.')
            return redirect('detalle_serie', serie_id=serie.id)

    return render(request, 'detalle_serie.html', {'serie': serie, 'comentarios': comentarios, 'comentario_form': comentario_form})

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    comentarios = ComentarioLibro.objects.filter(libro=libro)
    comentario_form = ComentarioFormLibro()

    if request.method == 'POST':
        comentario_form = ComentarioFormLibro(request.POST)
        if comentario_form.is_valid():
            nuevo_comentario = comentario_form.save(commit=False)
            nuevo_comentario.usuario = request.user
            nuevo_comentario.libro = libro
            nuevo_comentario.save()
            messages.success(request, 'Comentario agregado con éxito.')
            return redirect('detalle_libro', libro_id=libro.id)

    return render(request, 'detalle_libro.html', {'libro': libro, 'comentarios': comentarios, 'comentario_form': comentario_form})



def editar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)

    if request.user != pelicula.usuario:
        
        return redirect('lista_peliculas')  

    if request.method == 'POST':
        form = PeliculaFormulario(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('detalle_pelicula', pelicula_id=pelicula.id)  # Redirige a la página de detalles de la película
    else:
        form = PeliculaFormulario(instance=pelicula)

    return render(request, 'editar_pelicula.html', {'form': form})


def editar_serie(request, serie_id):
    serie = get_object_or_404(Serie, id=serie_id)

    if request.user != serie.usuario:
        
        return redirect('lista_series')  

    if request.method == 'POST':
        form = SerieFormulario(request.POST, request.FILES, instance=serie)
        if form.is_valid():
            form.save()
            return redirect('detalle_serie', serie_id=serie.id)  # Redirige a la página de detalles de la película
    else:
        form = SerieFormulario(instance=serie)

    return render(request, 'editar_serie.html', {'form': form})


def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.user != libro.usuario:
        
        return redirect('lista_libros')  

    if request.method == 'POST':
        form = LibroFormulario(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('detalle_libro', libro_id=libro.id)  # Redirige a la página de detalles de la película
    else:
        form = LibroFormulario(instance=libro)

    return render(request, 'editar_libro.html', {'form': form})




def eliminar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)

    if request.user == pelicula.usuario:
        pelicula.delete()

    return redirect('lista_peliculas')

def eliminar_serie(request, serie_id):
    serie = get_object_or_404(Serie, id=serie_id)

    if request.user == serie.usuario:
        serie.delete()

    return redirect('lista_series')

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Serie, id=libro_id)

    if request.user == libro.usuario:
        libro.delete()

    return redirect('libro_series')



