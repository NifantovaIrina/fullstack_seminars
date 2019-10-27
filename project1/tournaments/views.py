# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render, redirect

from tournaments.forms import TournamentForm
from tournaments.models import Tournament


def list_tournaments(request):
    tournaments = Tournament.objects.all()
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
            return redirect('/tournaments/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = TournamentForm()

    return render(request, 'create_tournament.html', {'form': form})


# Информация о конкретном турнире с возможностью ее редактировать. Видим, что код повторяется
# (выглядит почти так же, как для создания турнира).
def tournament_info(request, pk):
    tournament = Tournament.objects.get(pk=pk)
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
            tournament.save()
            return redirect('/tournaments/')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = TournamentForm({'name': tournament.name, 'date': tournament.date})
    return render(request, 'tournament_details.html', {'tour': tournament, 'form': form})


def main(request):
    return redirect('/tournaments/')