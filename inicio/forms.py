from django import forms

class CrearPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()

class CrearUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    informacion = forms.CharField(max_length=250)
    
class CrearAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    observacion = forms.CharField(max_length=250)
    patente = forms.CharField(max_length=10)
    
class BusquedaPaletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
    
class BusquedaUsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
    
class BusquedaAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)

    


