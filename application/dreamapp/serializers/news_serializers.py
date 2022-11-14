from rest_framework import serializers
from ..models import NewsData


class NewsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsData
        fields = ['id', 'date', 'author', 'topic', 'text']


class GetNewsDataSerializer(serializers.ModelSerializer):
    author = serializers.CharField(
        source="author.username", read_only=True)

    class Meta:
        model = NewsData
        fields = ['date', 'author', 'topic', 'text']


class PostNewsDataSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = NewsData
        fields = ['date', 'author', 'topic', 'text']
