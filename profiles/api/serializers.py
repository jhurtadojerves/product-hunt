from rest_framework import serializers

from ..models import Profile


class ProfileSerialzier(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True, source='user.username')
    first_name = serializers.CharField(source='user.first_name')

    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'bio',
            'location',
        )
