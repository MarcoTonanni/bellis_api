from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from battles.models import Battle
from battles.serializers import BattleModelSerializer, BattleListDetailSerializer


class BattleListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Battle.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BattleListDetailSerializer
        return BattleModelSerializer


class BattleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Battle.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BattleListDetailSerializer
        return BattleModelSerializer
