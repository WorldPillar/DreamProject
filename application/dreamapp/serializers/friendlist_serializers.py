from rest_framework import serializers
from ..models import FriendList


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList
        fields = ['id', 'owner', 'friend']


class GetFriendListSerializer(serializers.ModelSerializer):
    friend = serializers.CharField(
        source="friend.username", read_only=True)

    class Meta:
        model = FriendList
        fields = ['friend']
