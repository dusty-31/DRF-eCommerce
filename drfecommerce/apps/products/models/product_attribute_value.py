from django.db import models

from drfecommerce.apps.products.models.attribute_value import AttributeValue


class ProductAttributeValue(models.Model):
    attribute_value = models.ForeignKey(
        AttributeValue,
        on_delete=models.CASCADE,
        related_name="product_value_av",
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="producte_value_pl",
    )

    class Meta:
        unique_together = ("attribute_value", "product")
