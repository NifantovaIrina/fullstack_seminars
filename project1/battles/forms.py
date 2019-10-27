from django import forms

from tournaments.models import Tournament


class BattleForm(forms.Form):
    name = forms.CharField()
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all())