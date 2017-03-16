from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from preguntas.models import Equipo, Pregunta, Respuesta
from django.shortcuts import render

# Create your views here.

def get_answers(equipo, preguntas):
	
	result = []
	
	for pregunta in preguntas:
		
		try:
			answer = Respuesta.objects.get(equipo=equipo, pregunta=pregunta)
		except Respuesta.DoesNotExist:
			answer = None

		result.append(answer)

	return result


def index(request):

	es = Equipo.objects.all()
	equipos = {}
	preguntas = Pregunta.objects.all()
	for equipo in es:
		equipos[equipo.perfil.username] = get_answers(equipo, preguntas)

	context = {
		'equipos' : equipos,
		'preguntas' : preguntas
	}

	return render(request, 'score_index.html', context)

