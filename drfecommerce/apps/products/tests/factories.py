import factory

from drfecommerce.apps.products.models import (
    Attribute,
    AttributeValue,
    Brand,
    Category,
    Product,
    ProductImage,
    ProductLine,
    ProductType,
)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker('word')


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name = factory.Faker('word')

    @factory.post_generation
    def attribute(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.attribute.add(*extracted)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    description = factory.Faker('text')
    is_digital = factory.Faker('boolean')
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)
    product_type = factory.SubFactory(ProductTypeFactory)


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = factory.Faker('random_number', digits=2)
    sku = factory.Faker('word')
    stock_quantity = factory.Faker('random_number', digits=2)
    product = factory.SubFactory(ProductFactory)
    is_active = True

    @factory.post_generation
    def attribute_values(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.attribute_values.add(*extracted)


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    alternative_text = factory.Faker('word')
    url = factory.Faker('url')
    product_line = factory.SubFactory(ProductLineFactory)


class AttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attribute

    name = factory.Faker('word')
    description = factory.Faker('text')


class AttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AttributeValue

    value = factory.Faker('word')
    attribute = factory.SubFactory(AttributeFactory)
