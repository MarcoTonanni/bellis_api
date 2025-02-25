from rest_framework import serializers
from citations.models import Citation
from wars.serializers import WarModelSerializer


class CitationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Citation
        fields = '__all__'


class CitationListDetailSerializer(serializers.ModelSerializer):
    war = WarModelSerializer()

    class Meta:
        model = Citation
        fields = '__all__'
