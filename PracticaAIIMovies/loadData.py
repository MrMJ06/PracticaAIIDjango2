import sys, os, django
sys.path.append("/path/to/store") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PracticaAIIMovies.settings")
django.setup()

from practica.models import *
import pandas as pd

movies = pd.read_csv('data/movies.csv')
links = pd.read_csv('data/links.csv')
ratings = pd.read_csv('data/ratings.csv')
tags = pd.read_csv('data/tags.csv')
movies = movies.join(links.set_index('movieId'), on='movieId')
print(movies.head())
for i, movie in movies.iterrows():
    genres = []
    for genre in movie['genres'].split("|"):
        print(genre)
        g = Genre.objects.get_or_create(value=genre)
        print(g[0])
        genres.append(g[0])
    if pd.isnull(movie['imdbId']):
        movie['imdbId'] = None
    if pd.isnull(movie['tmdbId']):
        movie['tmdbId'] = None
    print(movie)
    m = Movie.objects.create(movie_id=movie['movieId'], title=movie['title'], imdb_id=movie['imdbId'], tmdb_id=movie['tmdbId'])
    m.genres.set(genres)
    m.save()

# for i, rating in ratings.iterrows():
#     print(rating)
#     user = User.objects.get_or_create(user_id=rating['userId'])
#     r = Rating.objects.create(user_id=user[0], movie_id=Movie.objects.get(movie_id=rating['movieId']), rating=rating['rating'], timestamp=rating['timestamp'])
#     r.save()
#     if i == 500:
#         break

for i, tag in tags.iterrows():
    print(tag)
    user = User.objects.get_or_create(user_id=tag['userId'])
    t = Tag.objects.create(user_id=user[0], movie_id=Movie.objects.get(movie_id=tag['movieId']), tag=tag['tag'], timestamp=tag['timestamp'])
    t.save()
    if i == 500:
        break



