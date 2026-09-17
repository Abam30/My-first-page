from django.shortcuts import render
from django.http import HttpResponse
def page (request):
    return HttpResponse ('<h1> ¡Hola!, Esta es la página principal de SOLARS. </h1>')
