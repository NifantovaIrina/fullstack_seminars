from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from battles.models import Battle
from battles.serializers import BattleSerializer
from tournaments.models import Tournament


class TournamentSerializer(serializers.ModelSerializer):
    battles = PrimaryKeyRelatedField(many=True, queryset=Battle.objects.all())
    # or
    # battles = BattleSerializer(many=True)

    class Meta:
        model = Tournament
        fields = ['name', 'date', 'battles']