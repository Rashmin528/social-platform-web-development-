from django.http import HttpResponse
from django.shortcuts import render

def posts_home(request):
	return render(request, 'basepeople.html')

def posts_nikola(request):
	return render(request, 'content/nikola.html')

def posts_Gravitational_waves(request):
	return render(request, 'content/Gravitational_waves.html')

def posts_neutrino(request):
	return render(request, 'content/neutrino.html')

def posts_Wormhole(request):
	return render(request, 'content/Wormhole.html')

def posts_stringtheory(request):
	return render(request, 'content/stringtheory.html')

def posts_einstein(request):
	return render(request, 'content/einstein.html')

def posts_bigbang(request):
	return render(request, 'content/bigbang.html')

def posts_cosmology(request):
	return render(request, 'content/cosmology.html')

def posts_jupitar(request):
	return render(request, 'content/jupitar.html')

def posts_fourthdim(request):
	return render(request, 'content/fourthdim.html')

def posts_titan(request):
	return render(request, 'content/titan.html')

def posts_faraday(request):
	return render(request, 'content/faraday.html')

def posts_regulus(request):
	return render(request, 'content/regulus.html')

def posts_nebula(request):
	return render(request, 'content/nebula.html')

def posts_sirius(request):
	return render(request, 'content/sirius.html')

