from django.db.models import Prefetch
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from drfecommerce.apps.products.models import Product
from drfecommerce.apps.products.serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    serializer_class = ProductSerializer
    queryset = Product.active_objects.all()
    lookup_field = 'slug'

    @extend_schema(responses=serializer_class)
    def retrieve(self, request: HttpRequest, slug: str = None) -> Response:
        """
        An endpoint to get a single product.
        """
        product = get_object_or_404(
            self.queryset.select_related('category')
            .prefetch_related(Prefetch('product_lines__product_images'))
            .prefetch_related(Prefetch('product_lines__attribute_values_attribute')),
            slug=slug,
        )
        serializer = self.serializer_class(product)
        return Response(data=serializer.data)

    @extend_schema(responses=serializer_class)
    def list(self, request: HttpRequest) -> Response:
        """
        An endpoint to get all products.
        """
        serializer = self.serializer_class(self.queryset.select_related('brand', 'category'), many=True)
        return Response(data=serializer.data)

    @action(methods=['get'], detail=False, url_path=r'category/(?P<slug>[\w-]+)/all', url_name='all')
    def get_list_product_by_category_slug(self, request: HttpRequest, slug: str = None) -> Response:
        """
        An endpoint to get all products by category slug.
        """
        serializer = ProductSerializer(
            self.queryset.filter(category__slug=slug).select_related('category'),
            many=True,
        )
        return Response(data=serializer.data)
