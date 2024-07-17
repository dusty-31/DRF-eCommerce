import factory

from drfecommerce.apps.products.models import Brand, Category, Product, ProductImage, ProductLine


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker('word')


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    description = factory.Faker('text')
    is_digital = factory.Faker('boolean')
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = factory.Faker('random_number', digits=2)
    sku = factory.Faker('word')
    stock_quantity = factory.Faker('random_number', digits=2)
    product = factory.SubFactory(ProductFactory)
    is_active = True


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    alternative_text = factory.Faker('word')
    url = factory.Faker('url')
    product_line = factory.SubFactory(ProductLineFactory)
