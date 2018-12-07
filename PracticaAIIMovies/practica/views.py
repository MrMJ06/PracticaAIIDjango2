from django.db.models import Sum
from django.shortcuts import render
from practica.models import *
from itertools import islice
# Create your views here.


def list_movies(request):
    movies = Movie.objects.all()

    return render(request, 'practica/movie_list.html', {'movies': movies})


def list_movies_by_genre(request):
    movies = dict()
    genres = Genre.objects.all()
    for genre in genres:
        print(len(genre.movie_set.all()))
        movies[genre.value] = genre.movie_set.all()
    print(movies)
    return render(request, 'practica/movie_list_genre.html', {'genres': movies})


def best_score_movies(request):
    top_dict = dict()
    result = dict()
    movies = Movie.objects.all()
    for movie in movies:
        mean_score = movie.rating_set.aggregate(Sum('rating'))['rating__sum']

        if len(movie.rating_set.all()) > 0:
            mean_score = mean_score/len(movie.rating_set.all())

        if mean_score is not None:
            top_dict[movie] = mean_score

    top = sorted(top_dict, key=top_dict.get, reverse=True)[:3]

    for movie in top:
        result[movie] = top_dict[movie]
    print(result)
    return render(request, 'practica/movie_top.html', {'top': result})

