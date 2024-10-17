from rest_framework import serializers

from drfecommerce.apps.products.models import Product
from drfecommerce.apps.products.models.attribute import Attribute
from drfecommerce.apps.products.serializers import AttributeSerializer
from drfecommerce.apps.products.serializers.product_line import ProductLineSerializer


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_lines = ProductLineSerializer(many=True)
    attribute = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'description',
            'is_digital',
            'brand_name',
            'category_name',
            'is_active',
            'product_lines',
            'attribute',
        ]

    def get_attribute(self, instance):
        product_type = instance.product_type
        attributes = Attribute.objects.filter(product_type_attributes__product_type=product_type)
        return AttributeSerializer(attributes, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        attribute_values = {item['id']: item['name'] for item in data.pop('attribute')}
        data['type specifications'] = attribute_values
        return data
