from django.shortcuts import render, redirect

from battles.forms import BattleForm
from battles.models import Battle


def list_battles(request):
    battles = Battle.objects.all()
    # print(battles[0])
    return render(request, 'list_battles.html', {'battles': battles})


def create_battle(request):
    if request.method == 'POST':
        form = BattleForm(request.POST)
        if form.is_valid():
            print("form data ", form.cleaned_data)
            battle = Battle(name=form.cleaned_data['name'])
            if form.cleaned_data['tournament'] is not None:
                battle.tournament = form.cleaned_data['tournament']
            battle.save()
            if form.cleaned_data['participants'] is not None:
                battle.participants.set(form.cleaned_data['participants'])
            return redirect('/battles/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BattleForm()

    return render(request, 'create_battle.html', {'form': form})


