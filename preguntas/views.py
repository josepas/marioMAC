from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
	
	return render(request, 'preg_index.html')


def pregunta(request, name):

	if request.method == 'POST':
		pass

	else:
		pregunta = get_object_or_404(Pregunta, nombre=name)


		# context = {
		# 	"pregunta" : pregunta
		# }

		# return render(request, 'pregunta.html', context)


