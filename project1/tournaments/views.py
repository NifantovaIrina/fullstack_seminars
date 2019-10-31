# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from battles.forms import BattleForm
from battles.models import Battle
from tournaments.forms import TournamentForm
from tournaments.models import Tournament


def list_tournaments(request):
    tournaments = Tournament.objects.all()
    for tournament in tournaments:
        print(tournament.battle_set)
        # print(tournament.__dict__)
    # Все шаблоны - в директории templates.
    return render(request, 'tournaments_list.html', {'tournaments': tournaments})


def create_tournament(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TournamentForm(request.POST)
        # check whether it's valid (use default validators for form fields with used types):
        if form.is_valid():
            # date field is not required in this form, fill it with current date if not provided
            if form.cleaned_data['date'] is None:
                date = datetime.date.today()
            else:
                date = form.cleaned_data['date']
            # store created object in database
            tournament = Tournament(name=form.cleaned_data['name'], date=date)
            tournament.save()
            tournament.battle_set.set(form.cleaned_data['battles'])
            print(tournament.battle_set.all())
            return redirect('/tournaments/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = TournamentForm()

    return render(request, 'create_tournament.html', {'form': form})


# Информация о конкретном турнире с возможностью ее редактировать. Видим, что код повторяется
# (выглядит почти так же, как для создания турнира).
def tournament_info(request, pk):
    tournament = Tournament.objects.get(pk=pk)
    print(tournament.pk)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TournamentForm(request.POST)
        # check whether it's valid (use default validators for form fields with used types):
        if form.is_valid():
            # date field is not required in this form, fill it with current date if not provided
            if form.cleaned_data['date'] is None:
                date = datetime.date.today()
            else:
                date = form.cleaned_data['date']
            # update current tournament in database
            tournament.name = form.cleaned_data['name']
            tournament.date = date
            print(form.cleaned_data['battles'])
            tournament.battle_set.set(form.cleaned_data['battles'])
            tournament.save()
            return redirect('/tournaments/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = TournamentForm({'name': tournament.name, 'date': tournament.date})
    return render(request, 'tournament_details.html', {'tour': tournament, 'form': form})


def add_battle(request, pk, battle_pk):
    tournament = Tournament.objects.get(pk=pk)
    battle = Battle.objects.get(pk=battle_pk)
    tournament.battle_set.add(battle)
    return HttpResponse("Success")


def create_battle(request, pk):
    if request.method == 'POST':
        form = BattleForm(request.POST)
        if form.is_valid():
            print("form data ", form.cleaned_data)
            battle = Battle(name=form.cleaned_data['name'], tournament=pk)
            battle.save()
            return redirect('/battles/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = BattleForm()

    return render(request, 'create_battle.html', {'form': form})


def main(request):
    return redirect('/tournaments/')