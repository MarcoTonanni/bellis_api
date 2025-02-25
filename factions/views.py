from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from factions.models import Faction
from factions.serializers import FactionSerializer


class FactionListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer


class FactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer


class FactionStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Faction.objects.all()

    def get(self, request):
        total_factions = self.queryset.count()

        return response.Response(
            data={'total_factions': total_factions},
            status=status.HTTP_200_OK,
        )
