from rest_framework import serializers

from drfecommerce.apps.products.models import Product
from drfecommerce.apps.products.serializers.product_line import ProductLineSerializer


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_lines = ProductLineSerializer(many=True)

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
        ]
