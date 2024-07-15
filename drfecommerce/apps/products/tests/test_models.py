import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    """
    Test the category model.
    """

    def test_str_method(self, category_factory):
        category_object = category_factory()
        assert str(category_object) == category_object.name


class TestBrandModel:
    """
    Test the brand model.
    """

    def test_str_method(self, brand_factory):
        brand_object = brand_factory()
        assert str(brand_object) == brand_object.name


class TestProductModel:
    """
    Test the product model.
    """

    def test_str_method(self, product_factory):
        product_object = product_factory()
        assert str(product_object) == product_object.name


class TestProductLineModel:
    """
    Test the product line model.
    """

    def test_str_method(self, product_line_factory):
        product_line_object = product_line_factory()
        assert str(product_line_object) == f'Name: {product_line_object.product.name} | SKU: {product_line_object.sku}'

    def test_order_field(self, product_line_factory, product_factory):
        product = product_factory()
        product_line_1 = product_line_factory(product=product)
        product_line_2 = product_line_factory(product=product)
        assert product_line_1.order == 1
        assert product_line_2.order == 2
        assert product_line_1.order != product_line_2.order

    def test_duplicate_order_values(self, product_line_factory, product_factory):
        product = product_factory()
        product_line_factory(order=1, product=product)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=product).clean()
