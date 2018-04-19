from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Page
import urllib.parse
import urllib.request

formulario = """
<form action="" method="POST">
    <input type="text" name="URL" value=""><br>
    <input type="submit" value="Enviar">
</form>
"""
@csrf_exempt
def mostrar(request):
    lista = Page.objects.all()
    max_longitud = 0

    if request.method == "POST":
        direccion = urllib.parse.unquote(str(request.body).split('=')[1][:-1])

        if direccion[0:4] == 'www.':
            direccion = 'http://' + direccion
        elif direccion[0:4] != 'http':
            direccion = 'http://www.' + direccion

        try:
            dir_acortada = Page.objects.get(direccion=direccion)
            return HttpResponse("La página ya existe.")
        except:
            for longitud in lista:
                max_longitud +=  1
            dir_acortada = "http://127.0.0.1:8000/" + str(max_longitud+1)
            p = Page(direccion = direccion, dir_acortada = dir_acortada)
            p.save()

        return HttpResponse(p.direccion + " " + p.dir_acortada)

    paginas = Page.objects.all()    #lista de viajes
    respuesta = "Listado de páginas: <br><ul>"
    for pagina in paginas:
        respuesta += "<li><a href= '/paginas/" + str(pagina.id) + "'>" + pagina.direccion + '</a>'+ " -> " + "<a href='" + str(pagina.dir_acortada) + "'>" + str(pagina.dir_acortada) + "</a>"
    respuesta += "</ul>"

    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + "    " + "<a href= '/logout'>Logout</a>"
        return HttpResponse(logged + "<br><br>Introduzca una url:" + formulario + respuesta)
    else:
        logged = 'Not logged in.' + "<a href='/login'>Login</a>"
        return HttpResponse(logged + "<br><br>" + respuesta)


def redireccion(request, numero):
    try:
        dir_acortada = 'http://127.0.0.1:8000/' + numero
        direccion = str(Page.objects.get(dir_acortada = dir_acortada))
    except DoesNotExits:
        return HttpResponse("No Existe")

    with urllib.request.urlopen(direccion) as r:
        pagina = r.read().decode('utf-8')

    return HttpResponse(pagina)
