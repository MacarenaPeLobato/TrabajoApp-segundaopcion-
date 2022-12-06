from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here. def familiares (request):

def basefamiliares (request):
    familia= Familia(nombrepadre="Ruben", nombremadre="Maria", nombrehijo="Emanuel", nombrehija="Ayelen", dnipadre="123456789", dnimadre="987654321", cumplehijo="27/07/2022", cumplehija="11/06/1996")
    familia.save()
    familia1= f"La familia esta compuesta por: {familia.nombrepadre}, {familia.nombremadre}, {familia.nombrehijo} y por ultimo {familia.nombrehija}. El DNI de la madre es {familia.dnimadre} y el de su padre es {familia.dnipadre}. La hija cumple el dia: {familia.cumplehija} y el hijo cumple: {familia.cumplehijo}"
    return HttpResponse(familia1)

def probandoapp (request):
    apellidito = "Penlob"
    familiares = ["Ruben", "Maria", "Ayelen", "Emanuel"]
    edades = ["26","29", "64", "64"]
    ruta= open("C://Users//fedef//Desktop//MACA PYTHON//AppFamilia//ProyectoFamilia//Plantillas//template.html")
    template= Template(ruta.read())
    ruta.close()
    contexto= Context({"Apellido": apellidito, "NombreFamiliares": familiares, "Edades": edades})
    documento= template.render(contexto)
    return HttpResponse(documento)

    