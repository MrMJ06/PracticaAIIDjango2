from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('discograficaSave/', views.formulario_discograficas),
    path('usuarioSave/', views.formulario_usuario),
    path('artistaSave/', views.formulario_artista),
    path('tiempoSave/', views.formulario_tiempo),
    path('artistas/', views.artistas_por_discografica),
    path('artistas-populares/', views.artistas_populares),
    path('buscador/', views.buscador_artistas_por_usuario),
]