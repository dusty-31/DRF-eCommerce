from rest_framework import serializers

from drfecommerce.apps.products.models import Brand, Category, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = [
            'id',
        ]


class ProductLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        exclude = [
            'id',
            'product',
            'is_active',
        ]


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_lines = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'is_digital',
            'brand_name',
            'category_name',
            'is_active',
            'product_lines',
        ]
