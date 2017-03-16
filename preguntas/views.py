from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Pregunta, Respuesta, Equipo

# Create your views here.

def index(request):
	
	return render(request, 'preg_index.html')


def pregunta(request, id):

	pregunta = get_object_or_404(Pregunta, id=id)

	if request.method == 'POST':


		if request.POST['codigo'] == "shame":
			pregunta = get_object_or_404(Pregunta, nombre=pregunta.clave)
			context = {
				"pregunta" : pregunta
			}
			return redirect('pregunta', id=pregunta.id)

		# Acertaron
		if request.POST['codigo'] == pregunta.clave:
			equipo = Equipo.objects.get(perfil=request.user)
			respuesta = Respuesta(equipo=equipo, pregunta=pregunta)
			respuesta.save()
			pregunta = get_object_or_404(Pregunta, nombre=pregunta.clave)
			context = {
				"pregunta" : pregunta
			}
			return redirect('pregunta', id=pregunta.id)

	context = {
		"pregunta" : pregunta
	}

	return render(request, 'preg_index.html', context)


