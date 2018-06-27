from rest_framework import serializers

from profiles.api.serializers import ProfileSerialzier
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = ProfileSerialzier(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'owner',
            'title',
            'description',
            'url',
            'pub_date',
        )
