# Generated by Django 4.2.6 on 2023-10-29 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_automovil_usuarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]
