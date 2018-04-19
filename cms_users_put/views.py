from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Page
import urllib.parse
import urllib.request


def mostrar(request):
    respuesta = "<ul>"
    for listado in Page.objects.all():
        respuesta += "<li>" + str(listado.nombre)
    respuesta += "</ul>"
    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + "    " + "<a href= '/logout'>Logout</a>"
        return HttpResponse(logged + "<br><br>Introduzca una url:" + formulario + respuesta)
    else:
        logged = 'Not logged in.' + "<a href='/login'>Login</a>"
        return HttpResponse(logged + "<br><br>" + respuesta)

@csrf_exempt
def insertar(request, texto):
    if request.method == "GET":
        try:
            p = Page.objects.get(nombre = texto)
            print()
            return HttpResponse(p.pagina)
        except Page.DoesNotExist:
            return HttpResponse("No existe una página para ese recurso.")

    else:
        if request.user.is_authenticated():
            p = Page(nombre = texto, pagina = request.body.decode('utf-8'))
            p.save()
            return HttpResponse("Página con el nombre: '" + str(p.nombre) + "' y el cuerpo: " + str(p.pagina) + " ha sido creada.")
        else:
            return HttpResponse("Necesitas estar logueado para modificar una página")
