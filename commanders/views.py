from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from commanders.models import Commander
from commanders.serializers import CommanderModelSerializer


class CommanderListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Commander.objects.all()
    serializer_class = CommanderModelSerializer


class CommanderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Commander.objects.all()
    serializer_class = CommanderModelSerializer
