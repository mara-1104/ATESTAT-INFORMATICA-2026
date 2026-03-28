from django.shortcuts import render, get_object_or_404
from .models import Activitate

def acasa_view(request):
    activitati = Activitate.objects.all()[:3]
    return render(request, "acasa.html", {"activitati": activitati})

def lista_activitati_view(request):
    activitati = Activitate.objects.all()
    return render(request, "activitati.html", {"activitati": activitati})

def activitate_detalii_view(request, id):
    activitate = get_object_or_404(Activitate, id=id)
    return render(request, "activitate_detalii.html", {"activitate": activitate})

def despre_view(request):
    return render(request, "despre.html")