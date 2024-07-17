import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from drfecommerce.apps.products.tests.factories import (
    BrandFactory,
    CategoryFactory,
    ProductFactory,
    ProductImageFactory,
    ProductLineFactory,
)

# Register factories

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
register(ProductLineFactory)
register(ProductImageFactory)


# Define fixtures


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()
