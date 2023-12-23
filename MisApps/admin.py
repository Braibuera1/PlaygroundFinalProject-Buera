from django.contrib import admin

from django.contrib import admin
from . import models

admin.site.register(models.Pelicula)
admin.site.register(models.Serie)
admin.site.register(models.Libro)
