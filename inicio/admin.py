from django.contrib import admin
from inicio.models import Paleta, Usuario, Auto

# Register your models here.

admin.site.register([Paleta, Usuario, Auto])