from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from preguntas.models import Equipo, Pregunta, Respuesta
from django.shortcuts import render

# Create your views here.

def get_answers(equipo):
	
	result = []
	
	preguntas = Pregunta.objects.all()
	for pregunta in preguntas:
		answer = Respuesta.objects.get(equipo=equipo, pregunta=pregunta)
		result.append(answer)

	return result


def index(request):

	es = Equipo.objects.all()
	equipos = {}
	for equipo in es:
		equipos[equipo.name] = get_answers(equipo)

	context = {
		'equipos' : equipos
	}

	return render(request, context)

