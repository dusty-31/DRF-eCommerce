import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from drfecommerce.apps.products.tests.factories import (
    AttributeFactory,
    AttributeValueFactory,
    CategoryFactory,
    ProductFactory,
    ProductImageFactory,
    ProductLineFactory,
    ProductTypeFactory,
)

# Register factories

register(CategoryFactory)
register(ProductFactory)
register(ProductLineFactory)
register(ProductImageFactory)
register(ProductTypeFactory)
register(AttributeValueFactory)
register(AttributeFactory)


# Define fixtures


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()
