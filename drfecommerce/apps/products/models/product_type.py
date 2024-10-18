from django.db import models

from drfecommerce.apps.products.models.attribute import Attribute
from drfecommerce.apps.products.models.product_type_attribute import ProductTypeAttribute


class ProductType(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    attribute = models.ManyToManyField(
        to=Attribute,
        through=ProductTypeAttribute,
        related_name="product_type_attribute",
    )

    def __str__(self):
        return self.name
