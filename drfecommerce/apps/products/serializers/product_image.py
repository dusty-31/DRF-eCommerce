from rest_framework import serializers

from drfecommerce.apps.products.models import ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = [
            'id',
            'product_line',
        ]
