from django.db import models


# Create your models here.
class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=200, unique=True)


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    imdb_id = models.IntegerField(null=True)
    tmdb_id = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre)


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)


class Tag(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    tag = models.CharField(max_length=200)
    timestamp = models.IntegerField()


class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.IntegerField()