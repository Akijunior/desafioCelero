from django.db import models


# Create your models here.

class Game(models.Model):
    games = models.CharField(max_length=200)
    year = models.IntegerField("Ano do Jogo")
    season = models.CharField("Estação", max_length=200)
    city = models.CharField("Cidade", max_length=200)
    sports = models.ManyToManyField("athlete.Sport")


class Athlete(models.Model):
    athlete_id = models.IntegerField("Id do atleta", unique=True)
    name = models.CharField("Nome", max_length=100)
    sex = models.CharField("Sexo", max_length=1)
    age = models.IntegerField("Idade")
    height = models.IntegerField("Altura")
    weight = models.IntegerField("Peso")
    team = models.CharField("Equipe/País", max_length=100)
    noc = models.CharField("Siglas", max_length=3)


class Sport(models.Model):
    sport = models.CharField(max_length=100)


class Medal(models.Model):
    athlete = models.ForeignKey('athlete.Athlete', on_delete=models.CASCADE)
    sport = models.ForeignKey('athlete.Sport', on_delete=models.CASCADE)
    event = models.CharField(max_length=100)
    medal = models.CharField(max_length=10)
