from django.shortcuts import render
from utils import limpiar_texto
from django.http import HttpResponse
def page (request):
    HttpResponse ('<h1> ¡Hola!, Esta es la página principal de SOLARS. </h1>')
    hola = "B I E N V E N I D O"
    texto = hola + "::" + limpiar_texto(hola)
    #return HttpResponse (texto.encode("utf-8"), content_type="text/plain")
    return render(request, "code.html", {"text": limpiar_texto(hola)})