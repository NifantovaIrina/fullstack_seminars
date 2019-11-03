# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from battles.forms import BattleForm
from battles.models import Battle
from tournaments.forms import TournamentForm
from tournaments.models import Tournament
from tournaments.serializers import TournamentSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


@api_view(['GET'])
def main(request):
    return Response({"Pong"})