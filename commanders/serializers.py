from rest_framework import serializers
from commanders.models import Commander


class CommanderModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commander
        fields = '__all__'

    def validate_birth(self, value):
        if value:
            if value.year >= 715:
                raise serializers.ValidationError('The Republic lasted until 727 A.U.C., no commander of its battles could have been born so late in its history')
        return value
