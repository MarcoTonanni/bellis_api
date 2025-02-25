from django.db.models import Avg
from rest_framework import serializers
from wars.models import War
from commanders.serializers import CommanderModelSerializer
from factions.serializers import FactionSerializer


class WarModelSerializer(serializers.ModelSerializer):
    sources_reliability = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = War
        fields = '__all__'

    def get_sources_reliability(self, obj):
        sources_reliability = obj.citations.aggregate(Avg('reliability'))['reliability__avg']

        if sources_reliability:
            return round(sources_reliability, 1)

        return None

    def validate_start_date(self, value):
        if value.year > 753:
            raise serializers.ValidationError("The Roman Republic lasted until 727 A.U.C., wars after this date don't belong to this period")
        return value

    def validate_end_date(self, value):
        if value.year > 753:
            raise serializers.ValidationError("The Roman Republic lasted until 727 A.U.C., wars after this date don't belong to this period")
        return value


class WarListDetailSerializer(serializers.ModelSerializer):
    commanders = CommanderModelSerializer(many=True)
    belligerents = FactionSerializer(many=True)
    victor = FactionSerializer()
    sources_reliability = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = War
        fields = ['id', 'name', 'sources_reliability', 'start_date', 'end_date', 'belligerents', 'victor', 'commanders']

    def get_sources_reliability(self, obj):
        sources_reliability = obj.citations.aggregate(Avg('reliability'))['reliability__avg']

        if sources_reliability:
            return round(sources_reliability, 1)

        return None
