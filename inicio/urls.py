from django.urls import path
from inicio.views import inicio, paleta, usuarios, automovil

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paleta, name= 'paletas'),
    path('usuarios/', usuarios, name='usuarios'),
    path('automovil/', automovil, name='automovil')
]
