from django.shortcuts import render, redirect

from inicio.models import Paleta, Usuario, Auto

from inicio.forms import CrearPaletaFormulario, CrearUsuarioFormulario, CrearAutoFormulario

from inicio.forms import BusquedaPaletaFormulario, BusquedaUsuarioFormulario, BusquedaAutoFormulario

# Create your views here.

def inicio(request):

    # v2
    # template = loader.get_template('inicio.html')
    # template_renderizado = template.render({})

    # return HttpResponse(template_renderizado)
    
    # v3
    return render(request, 'inicio/inicio.html', {})

def paleta(request):
    
    formulario = BusquedaPaletaFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_paletas = Paleta.objects.filter(marca__icontains = marca_a_buscar)

    return render(request, 'inicio/paletas.html', {'listado_de_paletas': listado_de_paletas})

def automovil(request):
    
    formulario = BusquedaAutoFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_autos = Auto.objects.filter(marca__icontains = marca_a_buscar)

    return render(request, 'inicio/automovil.html', {'listado_de_autos': listado_de_autos})
    
def usuarios(request):
    
    formulario = BusquedaUsuarioFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        listado_de_usuarios = Usuario.objects.filter(nombre__icontains = nombre_a_buscar)

    return render(request, 'inicio/usuarios.html', {'listado_de_usuarios': listado_de_usuarios})

def crear_paleta(request):
    
    # v1
    # # print(request.GET)
    # # print(request.POST)
    #
    # if request.method == 'POST':
    
    #     marca = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')
    
    #     paleta = Paleta(marca=marca, descripcion=descripcion, anio=anio)
    #     paleta.save()
    
    # v2 (Django Form)
    if request.method == "POST":
        formulario = CrearPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            
            paleta = Paleta(marca=marca, descripcion=descripcion, anio=anio)
            paleta.save()
            
            return redirect ('paletas')
    
    
    formulario = CrearPaletaFormulario()
    return render(request, 'inicio/crear_paleta.html', {'formulario': formulario})

def crear_usuario(request):
    
    if request.method == "POST":
        formulario = CrearUsuarioFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            nombre = info_limpia.get('nombre')
            apellido = info_limpia.get('apellido')
            edad = info_limpia.get('edad')
            informacion = info_limpia.get('informacion')
            
            usuario = Usuario(nombre=nombre, apellido=apellido, edad=edad, informacion=informacion)
            usuario.save()
            
            return redirect ('usuarios')
    
    
    formulario = CrearUsuarioFormulario()
    return render(request, 'inicio/crear_usuario.html', {'formulario': formulario})

def crear_auto(request):
    
    if request.method == "POST":
        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            observacion = info_limpia.get('observacion')
            patente = info_limpia.get('patente')
            
            auto = Auto(marca=marca, observacion=observacion, patente=patente)
            auto.save()
            
            return redirect ('automovil')
    
    
    formulario = CrearAutoFormulario()
    return render(request, 'inicio/crear_auto.html', {'formulario': formulario})
