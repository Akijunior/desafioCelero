from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

from django.db.models.signals import post_save
from django.dispatch import receiver


class Game(models.Model):
    game_name = models.CharField(max_length=200)
    year = models.IntegerField("Ano do Jogo")
    season = models.CharField("Estação", max_length=200)
    city = models.CharField("Cidade", max_length=200)
    sports = models.ManyToManyField("athlete.Sport")

    class Meta:
        ordering = ['games', ]


class Athlete(models.Model):
    athlete_id = models.IntegerField("Id do atleta", unique=True)
    name = models.CharField("Nome", max_length=100)
    sex = models.CharField("Sexo", max_length=1)
    age = models.IntegerField("Idade")
    height = models.IntegerField("Altura")
    weight = models.IntegerField("Peso")
    team = models.CharField("Equipe/País", max_length=100)
    noc = models.CharField("Siglas", max_length=3)

    class Meta:
        ordering = ['athlete_id', ]


class Sport(models.Model):
    sport = models.CharField(max_length=100)

    class Meta:
        ordering = ['sport', ]


class Event(models.Model):
    sport = models.ForeignKey('athlete.Sport', on_delete=models.CASCADE)
    event = models.CharField(max_length=100)

class Medal(models.Model):
    athlete = models.ForeignKey('athlete.Athlete', on_delete=models.CASCADE)
    event = models.ForeignKey('athlete.Event', on_delete=models.CASCADE)
    medal = models.CharField(max_length=10)

    class Meta:
        ordering = ['athlete__athlete_id', ]


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print(Token.objects.filter(user__username='b@a.com'))
    if created:
        Token.objects.create(user=instance)