from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from battles.forms import BattleForm
from battles.models import Battle
from battles.serializers import BattleSerializer


class BattleViewSet(viewsets.ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer

#
# class BattleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Battle.objects.all()
#         serializer = BattleSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Battle.objects.all()
#         battle = get_object_or_404(queryset, pk=pk)
#         serializer = BattleSerializer(battle)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#          pass
#
#     def create(self, request):
#         serializer = BattleSerializer(data=request.data)
#         if serializer.is_valid():
#             battle = serializer.create(serializer.validated_data)
#             new_serializer = BattleSerializer(battle)
#             return Response(new_serializer.data)
#         else:
#             print(serializer.errors)
#         return Response("woof")
