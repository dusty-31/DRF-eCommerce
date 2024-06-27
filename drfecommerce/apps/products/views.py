from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from drfecommerce.apps.products.models import Brand, Category, Product
from drfecommerce.apps.products.serializers import BrandSerializer, CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing all categories.
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(data=serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing all brands.
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(data=serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing all products.
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(data=serializer.data)
