from rest_framework import serializers
from ..models import ServerData


class ServerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerData
        fields = ['ip', 'port', 'name']


class ServerDataWithCountSerializer(serializers.ModelSerializer):
    maximum = serializers.IntegerField()
    current = serializers.IntegerField()

    class Meta:
        model = ServerData
        fields = ['ip', 'port', 'name', 'maximum', 'current']


class UpdateServerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerData
        fields = ['ip', 'port']

    def update(self, instance, validated_data):
        instance.ip = validated_data.get("ip", instance.ip)
        instance.port = validated_data.get("port", instance.port)
        instance.save()
        return instance