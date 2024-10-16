from rest_framework import serializers

from drfecommerce.apps.products.models import Attribute


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['name']
