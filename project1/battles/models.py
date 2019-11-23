from django.db import models

from tournaments.models import Tournament
from django.contrib.auth.models import User


class Battle(models.Model):
    name = models.CharField(max_length=400)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE,
                                   blank=True, null=True, related_name='battles')
    participants = models.ManyToManyField(User, related_name='participants')