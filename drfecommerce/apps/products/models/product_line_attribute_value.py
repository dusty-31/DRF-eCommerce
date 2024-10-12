from django.db import models

from drfecommerce.apps.products.models.attribute_value import AttributeValue
from drfecommerce.apps.products.models.product_line import ProductLine


class ProductLineAttributeValue(models.Model):
    attribute_value = models.ForeignKey(to=AttributeValue, on_delete=models.CASCADE, related_name='attribute_values_av')
    product_line = models.ForeignKey(to=ProductLine, on_delete=models.CASCADE, related_name='attribute_values_pl')

    class Meta:
        unique_together = ('attribute_value', 'product_line')
        verbose_name = 'Product Line Attribute Value'
        verbose_name_plural = 'Product Line Attribute Values'
