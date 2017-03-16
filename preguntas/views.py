from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Pregunta

# Create your views here.

def index(request):
	
	return render(request, 'preg_index.html')


def pregunta(request, name):

	pregunta = get_object_or_404(Pregunta, nombre=name)

	if request.method == 'POST':

		# Acertaron
		if request.POST['codigo'] == pregunta.clave:
			pregunta = get_object_or_404(Pregunta, nombre=pregunta.clave)
			context = {
				"pregunta" : pregunta
			}
			return redirect('pregunta', name=pregunta.nombre)

	context = {
		"pregunta" : pregunta
	}

	return render(request, 'preg_index.html', context)


