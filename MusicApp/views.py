from django.shortcuts import render
from MusicApp.forms import BandaFormulario, MusicoFormulario, TemaFormulario
from django.http import HttpResponse
from MusicApp.models import Banda, Musico, Tema

# Create your views here.


def inicio(request):
    return render(request, 'padre.html')


def musicos(request):
    if request.method == 'POST':
        formulario = MusicoFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            musico = Musico(
                nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
        musico.save()
        return render(request, "padre.html")
    else:
        formulario = MusicoFormulario()
    return render(request, 'musicos.html', {"formulario": formulario})


def temas(request):
    if request.method == 'POST':
        formulario = TemaFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            tema = Tema(nombre=informacion['nombre'], duracion=informacion['duracion'],
                        añoLanzamiento=informacion['añoLanzamiento'], autor=informacion['autor'])
            tema.save()
            return render(request, "padre.html")
    else:
        formulario = TemaFormulario()
    return render(request, 'temas.html', {"formulario": formulario})


def bandas(request):
    if request.method == 'POST':
        formulario = BandaFormulario(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            banda = Banda(
                nombre=informacion['nombre'], genero=informacion['genero'], pais=informacion['pais'])
            banda.save()
            return render(request, "padre.html")
    else:
        formulario = BandaFormulario()
    return render(request, 'bandas.html', {"formulario": formulario})


def busquedaMusico(request):
    return render(request, 'busquedaMusico.html')


def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        musicos = Musico.objects.filter(nombre__icontains=nombre)
        return render(request, "resultadoBusqueda.html", {"musicos": musicos, "nombre": nombre})
    else:
        respuesta = "No enviaste datos"

    return render(request, "padre.html", {"respuesta":respuesta})
