from django.urls import path
from .views import activitate_detalii_view
from .views import lista_activitati_view
from .views import acasa_view

urlpatterns = [
    path('', acasa_view, name="acasa"),
    path('activitati/', lista_activitati_view, name="activitati"),
    path('activitati/<int:id>/', activitate_detalii_view, name="detail"),
]