from django.urls import path
from .views import activitate_detalii_view
from .views import lista_activitati_view
from .views import acasa_view

urlpatterns = [

	path("acasa", acasa_view),
	path("activitati", lista_activitati_view),
	path("detalii", activitate_detalii_view),
]
