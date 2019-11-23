from __future__ import unicode_literals

from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=400)
    date = models.DateField()

    # def __str__(self):
    #     return   self.name