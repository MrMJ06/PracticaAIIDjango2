from django.db.models import Sum, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from practica.models import *
from .forms.forms import *
from itertools import islice
# Create your views here.


def formulario_discograficas(request):
    if request.method == 'POST':
        form = DiscograficaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/practica/index")
    else:
        form = DiscograficaForm()
    return render(request, 'practica/form.html', {'form': form,'action':'/practica/discograficaSave/'})


def formulario_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/practica/index")
    else:
        form = ArtistaForm()
    return render(request, 'practica/form.html', {'form': form,'action':'/practica/artistaSave/'})


def formulario_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/practica/index")
    else:
        form = UsuarioForm()
    return render(request, 'practica/form.html', {'form': form,'action':'/practica/usuarioSave/'})


def formulario_tiempo(request):
    if request.method == 'POST':
        form = TiempoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/practica/index")
    else:
        form = TiempoForm()
    return render(request, 'practica/form.html', {'form': form,'action':'/practica/tiempoSave/'})


def index(request):

    return render(request, 'practica/index.html')


def artistas_por_discografica(request):
    result = dict()

    discograficas = Discografica.objects.all()

    for discografica in discograficas:
        result[discografica.nombre] = discografica.artista_set.all()
    print(result)
    return render(request, 'practica/artistas.html', {'artista': result})

def artistas_populares(request):
    Artista.objects.filter()
    artistas = Artista.objects.annotate(count_tiempos=Sum('tiempo')).order_by('-count_tiempos')[:2]

    return render(request, 'practica/artistas-populares.html', {'genres': artistas})

def buscador_artistas_por_usuario(request):
    if request.method == 'POST':
        form = Buscador(request.POST)
        if form.is_valid():
            Artista.objects.filter(tiempo__usuario__nombre_usuario__icontains=form['usuario'])
            return HttpResponseRedirect("/practica/index")
    else:
        form = Buscador()
    return render(request, 'practica/form.html', {'form': form,'action':'/practica/buscador/'})

# def list_movies_by_genre(request):
#     movies = dict()
#     genres = Genre.objects.all()
#     for genre in genres:
#         print(len(genre.movie_set.all()))
#         movies[genre.value] = genre.movie_set.all()
#     print(movies)
#     return render(request, 'practica/movie_list_genre.html', {'genres': movies})
#
#
# def best_score_movies(request):
#     top_dict = dict()
#     result = dict()
#     movies = Movie.objects.all()
#     for movie in movies:
#         mean_score = movie.rating_set.aggregate(Sum('rating'))['rating__sum']
#
#         if len(movie.rating_set.all()) > 0:
#             mean_score = mean_score/len(movie.rating_set.all())
#
#         if mean_score is not None:
#             top_dict[movie] = mean_score
#
#     top = sorted(top_dict, key=top_dict.get, reverse=True)[:3]
#
#     for movie in top:
#         result[movie] = top_dict[movie]
#     print(result)
#     return render(request, 'practica/movie_top.html', {'top': result})
#
#
# def search_movie(request):
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = search(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             movies = Movie.objects.filter(title__contains=form['title'].value()).all()
#
#             return render(request, 'practica/movie_list.html', {'movies': movies})
#
#         # if a GET (or any other method) we'll create a blank form
#     else:
#         form = search()
#
#     return render(request, 'practica/movie_form.html', {'form': form})