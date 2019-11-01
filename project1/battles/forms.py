from django import forms

from tournaments.models import Tournament
from django.contrib.auth.models import User


class BattleForm(forms.Form):
    name = forms.CharField()
    tournament = forms.ModelChoiceField(queryset=Tournament.objects.all(), required=False)
    participants = forms.ModelMultipleChoiceField(queryset=User.objects.all())