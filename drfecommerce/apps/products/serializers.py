from rest_framework import serializers

from drfecommerce.apps.products.models import Brand, Category, Product, ProductLine


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ['name', 'description', 'is_digital', 'brand', 'category', 'is_active']


class ProductLineSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductLine
        fields = '__all__'
