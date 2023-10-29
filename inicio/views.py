from django.shortcuts import render

from inicio.models import Paleta

# Create your views here.

def inicio(request):

    # v2
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})

    # return HttpResponse(template_renderizado)
    
    # v3
    return render(request, 'inicio/inicio.html', {})

def paleta(request):
    
    paleta = Paleta(marca='wilson', descripcion='paleta de bela', anio=2022)
    paleta.save()
    
    return render(request, 'inicio/paletas.html', {'paleta': paleta})

def automovil(request):
    
    return render(request, 'inicio/automovil.html')
    
def usuarios(request):
    
    return render(request, 'inicio/usuarios.html')