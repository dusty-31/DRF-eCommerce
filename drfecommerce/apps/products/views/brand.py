from django.http import HttpRequest
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from drfecommerce.apps.products.models import Brand
from drfecommerce.apps.products.serializers import BrandSerializer, CategorySerializer


class BrandViewSet(viewsets.ViewSet):
    model = Brand
    serializer_class = BrandSerializer
    """
    A simple ViewSet for viewing all brands.
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request: HttpRequest) -> Response:
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(data=serializer.data)
