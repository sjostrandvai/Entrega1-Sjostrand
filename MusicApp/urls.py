from django.urls import path
from MusicApp import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('musicos', views.musicos, name="Musicos"),
    path('bandas', views.bandas, name="Bandas"),
    path('temas', views.temas, name="Temas"),
    path('buscarMusico', views.busquedaMusico, name="Buscar Musico"),
    path('buscar', views.buscar, name="buscar")
]
