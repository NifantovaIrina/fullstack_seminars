from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.relations import PrimaryKeyRelatedField, StringRelatedField

from battles.models import Battle
from tournaments.models import Tournament


class BattleSerializer(serializers.ModelSerializer):
    tournament = PrimaryKeyRelatedField(queryset=Tournament.objects.all(),
                                          read_only=False)
    participants = PrimaryKeyRelatedField(many=True, queryset=User.objects.all(),
                                          read_only=False)
    id = IntegerField(read_only=True, source="pk")

    class Meta:
        model = Battle
        fields = ["name", "participants", "tournament", "id"]

    # def create(self, validated_data):
    #     print("custom create method!")
    #     battle = Battle(name=validated_data['name'],
    #                     tournament=validated_data['tournament'])
    #     battle.save()
    #     battle.participants.set(validated_data['participants'])
    #     print(battle)
    #     return battle



