from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def content(request, identificador):
    if request.method != "GET":
        return HttpResponse("Method not allowed", status=405)
    try:
        pag = Pages.objects.get(id = int(identificador))
        print(pag.page)
        return HttpResponse(pag.page)
    except ObjectDoesNotExist:
        return HttpResponse("Content not found", status=404)

def mostrar_Info(request):
    lista = Pages.objects.all()
    respuesta = "<ol>"
    for pag in lista:
        respuesta += '<li><a href="' + str(pag.id) + '">' + pag.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)

def msg_error(request, msg):
    return HttpResponse(msg + ": content not found", status=404)
