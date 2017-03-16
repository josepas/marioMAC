from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from preguntas.models import Equipo

# Create your views here.

def index(request):

	if request.method == 'POST':
		team_name = request.POST['equipo']
		password = request.POST['password']

		user = authenticate(username=team_name,password=password)

		if user is not None:
			if user.is_active:
				print("ENTREEEE")
				login(request, user)
				return render(request, 'instructivo.html')

	return render(request, 'index.html')

def logout_view(request):
	logout(request)
	return redirect('index')

def register(request):

	if request.method == 'POST':
		team_name = request.POST['equipo']
		password = request.POST['password']

		user = User.objects.create_user(team_name,password)
		user.save()

		team = Equipo(perfil=user)
		team.save()

		return redirect('index')
	
	return render(request, 'register.html')

def instructivo(request):
	
	return render(request, 'instructivo.html')