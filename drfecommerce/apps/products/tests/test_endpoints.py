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


class TestProductEndpoints:
    """
    Test the product endpoints.
    """

    endpoint = '/api/product/'

    def test_return_all_products(self, api_client, product_factory):
        product_factory.create_batch(5)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(response.json()) == 5

    def test_return_product_by_slug(self, api_client, product_factory):
        product = product_factory(name='Test Slug')
        response = api_client.get(f'{self.endpoint}{product.slug}/')
        assert response.status_code == 200
        assert response.json()['slug'] == 'test-slug'

    def test_return_products_by_category_slug(self, api_client, product_factory, category_factory):
        category = category_factory(name='Test Category')
        x = product_factory.create_batch(5, category=category)
        print(x)
        response = api_client.get(f'{self.endpoint}category/{category.slug}/all/')
        assert response.status_code == 200
        assert len(response.json()) == 5
