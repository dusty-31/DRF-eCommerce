import pytest

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    """
    Test the category endpoints.
    """

    endpoint = '/api/category/'

    def test_category_get(self, api_client, category_factory):
        category_factory.create_batch(5)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.json()) == 5


class TestBrandEndpoints:
    """
    Test the brand endpoints.
    """

    endpoint = '/api/brand/'

    def test_brand_get(self, api_client, brand_factory):
        brand_factory.create_batch(5)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.json()) == 5


class TestProductEndpoints:
    """
    Test the product endpoints.
    """

    endpoint = '/api/product/'

    def test_product_get(self, api_client, product_factory):
        product_factory.create_batch(5)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.json()) == 5
