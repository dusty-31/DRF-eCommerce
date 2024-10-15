from rest_framework import serializers

from drfecommerce.apps.products.models import ProductLine
from drfecommerce.apps.products.serializers.product_image import ProductImageSerializer


class ProductLineSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = [
            'price',
            'sku',
            'stock_quantity',
            'order',
            'product_images',
        ]
