from django.shortcuts import render
from django.http import HttpResponse
def index (request):
    return HttpResponse ('<h1> ¡Hola!, Esta es la página principal de Encuestas. </h1>')
# Create your views here.
