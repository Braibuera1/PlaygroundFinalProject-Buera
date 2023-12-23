from django.urls import path, include
from . import views
from .views import UsuarioEdicion, CambioPassword, PeliculaLista, SerieLista, LibroLista
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('CineClub/',views.inicio, name='pagina principal'),
    path('CineClub/login/',views.login_request, name='Login'),
    path('CineClub/about/',views.about, name='about'),
    path('CineClub/register/',views.register, name = 'register'),
    path('CineClub/logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('nueva_contraseña/', CambioPassword.as_view(), name='cambiar_contraseña'),
    path('cambio_exitoso/', views.password_exitoso, name='cambio_exitoso'),
    
    path('lista_peliculas/', PeliculaLista.as_view(), name='lista_peliculas'),
    path('lista_series/', SerieLista.as_view(), name='lista_series'),
    path('lista_libros/', LibroLista.as_view(), name='lista_libros'),
    
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('agregar_serie/', views.agregar_serie, name='agregar_serie'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),
    
    path('pelicula/<int:pelicula_id>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('serie/<int:serie_id>/', views.detalle_serie, name='detalle_serie'),
    path('libro/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    
    path('editar_pelicula/<int:pelicula_id>/', views.editar_pelicula, name='editar_pelicula'),
    path('editar_serie/<int:serie_id>/', views.editar_serie, name='editar_serie'),
    path('editar_libro/<int:libro_id>/', views.editar_libro, name='editar_libro'),
    
    path('eliminar_pelicula/<int:pelicula_id>/', views.eliminar_pelicula, name='eliminar_pelicula'),
    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),
    path('eliminar_serie/<int:serie>/', views.eliminar_serie, name='eliminar_serie'),
    
    
    
    
    
    
]