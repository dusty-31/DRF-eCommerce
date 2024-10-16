from rest_framework import serializers

from drfecommerce.apps.products.models import AttributeValue
from drfecommerce.apps.products.serializers.attribute import AttributeSerializer


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=False)

    class Meta:
        model = AttributeValue
        fields = ['attribute', 'value']
