from django.db.models import Count, Avg
from rest_framework import generics, views, status, response
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from wars.models import War
from wars.serializers import WarModelSerializer, WarListDetailSerializer
from citations.models import Citation


class WarListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = War.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WarListDetailSerializer
        return WarModelSerializer


class WarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = War.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WarListDetailSerializer
        return WarModelSerializer


class WarStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = War.objects.all()

    def get(self, request):
        total_wars = self.queryset.count()
        wars_by_victor = self.queryset.values('victor__name').annotate(count=Count('id'))
        average_reliability = Citation.objects.aggregate(avg_reliability=Avg('reliability'))['avg_reliability']

        return response.Response(data={
            'total_wars': total_wars,
            'wars_by_victor': wars_by_victor,
            'sources_average_reliability': round(average_reliability, 1) if average_reliability else 0,
        }, status=status.HTTP_200_OK)
