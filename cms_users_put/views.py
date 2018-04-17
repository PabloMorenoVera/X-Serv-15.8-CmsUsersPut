from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Viaje

formulario = """
<form action="" method="POST">
    Destino: <input type="text" name="destino"><br>
    Locomoción: <input type="text" name="locomocion" value="Avión"><br>
    Alojamiento: <input type="text" name="alojamiento"><br>
    Precio: <input type="text" name="precio"><br>
    <input type="submit" value="Enviar">
</form>
"""

def mostrar(request):
    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + "    " + "<a href= '/logout'>Logout</a>"
    else:
        logged = 'Not logged in.' + "<a href='/login'>Login</a>"
    viajes = Viaje.objects.all()    #lista de viajes
    respuesta = "Listado de viajes: <br><ul>"
    for viaje in viajes:
        respuesta += "<li><a href= '/viajes/viaje/" + str(viaje.id) + "'>" + viaje.destino + '</a>'
    respuesta += "</ul>"
    return HttpResponse(logged + "<br><br>" + respuesta)

@csrf_exempt
def viaje(request, number):
    if request.method == "POST":
        viaje = Viaje(locomocion = request.POST['locomocion'], destino = request.POST['destino'], alojamiento = request.POST['alojamiento'], precio = request.POST['precio'])
        viaje.save()
        number = viaje.id
    try:
        viaje = Viaje.objects.get(id=int(number))
    except Viaje.DoesNotExist:
        return HttpResponse("No existe")

    respuesta = "Viaje: " + viaje.destino + "<br>"
    respuesta += "Locomocion: " + viaje.locomocion + "<br>"
    respuesta += "ID: " + str(viaje.id) + "<br>"
    respuesta += "Precio: " + str(viaje.precio) + "euros" + "<br><br>"
    if request.user.is_authenticated():
        respuesta += formulario
    return HttpResponse(respuesta)

def logged(request):
    return HttpResponse("¡Bienvenido!")
