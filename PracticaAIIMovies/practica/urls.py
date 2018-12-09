from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.list_movies),
    path('moviesByGenres/', views.list_movies_by_genre),
    path('moviesTop/', views.best_score_movies),
    path('search/', views.search_movie),
]