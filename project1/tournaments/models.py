# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from project1 import settings


class Tournament(models.Model):
    name = models.CharField(max_length=400)
    date = models.DateField()