from rest_framework import serializers
from battles.models import Battle
from commanders.serializers import CommanderModelSerializer
from factions.serializers import FactionSerializer
from wars.serializers import WarModelSerializer


class BattleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Battle
        fields = '__all__'

    def validade_date(self, value):
        if value.year > 727:
            raise serializers.ValidationError('The Roman Republic lasted until 727 A.U.C., so no battle can have happened after that year')
        return value


class BattleListDetailSerializer(serializers.ModelSerializer):
    war = WarModelSerializer()
    belligerents = FactionSerializer(many=True)
    commanders = CommanderModelSerializer(many=True)
    victor = FactionSerializer()

    class Meta:
        model = Battle
        fields = '__all__'
