from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.response import Response

from battles.forms import BattleForm
from battles.models import Battle
from battles.serializers import BattleSerializer


class OwnerOrAdminPermission(BasePermission):
    def has_permission(self, request, view):
        print(view.action)
        print(request.method)
        print(request.user)
        print(request.user.is_staff)
        # raise PermissionDenied
        return True

    def has_object_permission(self, request, view, obj):
        print("check object permission")
        if request.user.is_staff or request.user in obj.participants.all():
            return True
        raise PermissionDenied


class BattleViewSet(viewsets.ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
    permission_classes = [OwnerOrAdminPermission]

    def get_object(self):
        print("my get_object called")
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        print("")
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        print("my get_queryset_called")
        print(self.request.user)
        return Battle.objects.filter(participants=self.request.user)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     return Response(BattleSerializer(queryset, many=True).data)
