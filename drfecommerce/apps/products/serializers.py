from rest_framework import serializers

from drfecommerce.apps.products.models import Brand, Category, Product, ProductImage, ProductLine


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


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = [
            'id',
            'product_line',
        ]


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
