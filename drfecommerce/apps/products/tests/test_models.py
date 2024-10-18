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


class TestProductTypeModel:
    """
    Test the product type model.
    """

    def test_str_method(self, product_type_factory):
        product_type_object = product_type_factory()
        assert str(product_type_object) == product_type_object.name


class TestAttributeModel:
    """
    Test the attribute model.
    """

    def test_str_method(self, attribute_factory):
        attribute_object = attribute_factory()
        assert str(attribute_object) == attribute_object.name


class TestAttributeValueModel:
    """
    Test the attribute value model.
    """

    def test_str_method(self, attribute_value_factory):
        attribute_value_object = attribute_value_factory()
        result = f'{attribute_value_object.attribute.name} - {attribute_value_object.value}'
        assert str(attribute_value_object) == result


class TestProductImageModel:
    """
    Test the product image model.
    """

    def test_str_method(self, product_image_factory):
        product_image_object = product_image_factory()
        str_method_example = f'Product Line: {product_image_object.product_line.sku} | Name: {product_image_object.url}'
        assert str(product_image_object) == str_method_example

    def test_order_field(self, product_image_factory, product_line_factory):
        product_line = product_line_factory()
        product_image_1 = product_image_factory(product_line=product_line)
        product_image_2 = product_image_factory(product_line=product_line)
        assert product_image_1.order == 1
        assert product_image_2.order == 2
        assert product_image_1.order != product_image_2.order
