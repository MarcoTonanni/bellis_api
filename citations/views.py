from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from citations.models import Citation
from citations.serializers import CitationSerializer, CitationListDetailSerializer


class CitationListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Citation.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CitationListDetailSerializer
        return CitationSerializer


class CitationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Citation.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CitationListDetailSerializer
        return CitationSerializer
