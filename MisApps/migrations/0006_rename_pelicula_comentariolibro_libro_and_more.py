# Generated by Django 4.2.7 on 2023-12-23 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MisApps', '0005_comentarioserie_comentariolibro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentariolibro',
            old_name='pelicula',
            new_name='libro',
        ),
        migrations.RenameField(
            model_name='comentarioserie',
            old_name='pelicula',
            new_name='serie',
        ),
    ]
