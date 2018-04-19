from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Page
import urllib.parse
import urllib.request
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def mostrar(request):
    respuesta = "<ul>"
    for listado in Page.objects.all():
        respuesta += "<li>" + str(listado.nombre)
    respuesta += "</ul>"
    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + "    " + "<a href= '/logout'>Logout</a>"
    else:
        logged = 'Not logged in.' + "<a href='/login'>Login</a>"
    return HttpResponse(logged + "<br><br>Contenido de la base de datos:<br>" + respuesta)

@csrf_exempt
def insertar(request, texto):
    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + "    " + "<a href= '/logout'>Logout</a>"
    else:
        logged = 'Not logged in.' + "<a href='/login'>Login</a>"

    if request.method == "GET":
        try:
            p = Page.objects.get(nombre = texto)
            return HttpResponse(logged + "<br><br>" + p.pagina)
        except Page.DoesNotExist:
            return HttpResponse(logged + "<br><br>No existe una página para ese recurso.")

    else:
        if request.user.is_authenticated():
            try:
                p = Page.objects.get(nombre = texto)
                p = Page(nombre = texto, pagina = request.body.decode('utf-8'))
                p.save()
                return HttpResponse("Página con el nombre: '" + str(p.nombre) + "' y el cuerpo: " + str(p.pagina) + " ha sido modificada.")
            except Page.DoesNotExist:
                p = Page(nombre = texto, pagina = request.body.decode('utf-8'))
                p.save()
                return HttpResponse("Página con el nombre: '" + str(p.nombre) + "' y el cuerpo: " + str(p.pagina) + " ha sido creada.")
        else:
            return HttpResponse(logged + "<br><br>Necesitas estar logueado para modificar una página")
