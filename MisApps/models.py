from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    def __str__(self):
        return self.titulo

class Serie(models.Model):
    titulo = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return self.titulo 
    
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return self.titulo     
    
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.usuario.username} - {self.fecha_creacion}'    
    
class ComentarioSerie(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.usuario.username} - {self.fecha_creacion}'  
    
class ComentarioLibro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.usuario.username} - {self.fecha_creacion}'        
