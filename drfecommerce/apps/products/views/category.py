from django.http import HttpRequest
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from drfecommerce.apps.products.models import Category
from drfecommerce.apps.products.serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing all categories.
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request: HttpRequest) -> Response:
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(data=serializer.data)
