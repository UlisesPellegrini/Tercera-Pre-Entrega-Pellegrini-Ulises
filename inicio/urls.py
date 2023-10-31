from django.urls import path
from inicio.views import inicio, paleta, crear_paleta, usuarios, crear_usuario, automovil, crear_auto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paleta, name= 'paletas'),
    path('usuarios/', usuarios, name='usuarios'),
    path('automovil/', automovil, name='automovil'),
    
    path('paletas/crear/', crear_paleta, name='crear_paleta'),
    path('usuarios/crear/', crear_usuario, name='crear_usuario'),
    path('automovil/crear/', crear_auto, name='crear_auto')
]
