from django.db import models

from tournaments.models import Tournament


class Battle(models.Model):
    name = models.CharField(max_length=400)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    participants = models.ManyToManyField('settings.AUTH_USER_MODEL')