from django.shortcuts import render

# Create your views here.

def acasa_view(request):
	context = {}
	return render(request, 'acasa.html.html', context)

def lista_activitati_view(request):
	context = {}
	return render(request, 'activitati.html.html', context)

def activitate_detalii_view(request):
	context = {}
	return render(request, 'activitate_detalii.html.html', context)
