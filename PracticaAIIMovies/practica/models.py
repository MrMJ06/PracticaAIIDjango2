from django.db import models


# Create your models here.
class Discografica(models.Model):
    discografica_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, unique=True)
    pais = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre


class Estilo(models.Model):
    estilo_id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.value


class Artista(models.Model):
    artista_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    discografica = models.ForeignKey(Discografica, on_delete=models.CASCADE)
    fecha = models.DateField()
    estilos = models.ManyToManyField(Estilo, default=[], blank=True)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.nombre + " " + self.apellidos


class Tiempo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    tiempo = models.IntegerField()

    def __str__(self):
        return self.tiempo