from django.http import HttpResponse
from django.shortcuts import render
from .models import personas
# Create your views here.

def familiares(request):
    familiar = personas(nombre ="Pablo", apellido = "Callejas", documento = 12345678, fechaDeNacimiento = "1990-01-12")
    familiar.save()
    familiar2 = personas(nombre ="Francesco", apellido = "Devitta", documento = 45678902, fechaDeNacimiento = "1993-01-12")
    familiar2.save()
    familiar3 = personas(nombre ="Lorena", apellido = "Perez", documento = 67811111, fechaDeNacimiento = "1996-01-12")
    familiar3.save()
    familia_list = personas.objects.all
    return render(request, 'familia.html', {'individual':familia_list})
