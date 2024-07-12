from django.shortcuts import render, HttpResponse
from django.http import request

# Create your views here


def index(request):
    return HttpResponse("Bienvenido a la aplicación de Finanzas.")

def detalle(request, id):
    return HttpResponse(f"Detalles del item con ID: {id}")