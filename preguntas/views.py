from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Pregunta, Respuesta, Equipo
import simpleaudio as sa

# Create your views here.

def index(request):
	
	return render(request, 'preg_index.html')


def pregunta(request, id):

	pregunta = get_object_or_404(Pregunta, id=id)

	if request.method == 'POST':


		if request.POST['codigo'] == "shame":
			pregunta = get_object_or_404(Pregunta, nombre=pregunta.clave)
			return redirect('pregunta', id=pregunta.id)

		# Acertaron
		if request.POST['codigo'] == pregunta.clave:
			equipo = Equipo.objects.get(perfil=request.user)
			respuesta = Respuesta(equipo=equipo, pregunta=pregunta)
			respuesta.save()
			pregunta = get_object_or_404(Pregunta, nombre=pregunta.clave)
			wave_obj = sa.WaveObject.from_wave_file("static/img/up.wav")
			play_obj = wave_obj.play()
			play_obj.wait_done()
			return redirect('pregunta', id=pregunta.id)

	context = {
		"pregunta" : pregunta
	}

	return render(request, 'preg_index.html', context)


