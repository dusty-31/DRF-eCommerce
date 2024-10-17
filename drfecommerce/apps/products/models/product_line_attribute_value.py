from django.db import models
from rest_framework.exceptions import ValidationError

from drfecommerce.apps.products.models import Attribute
from drfecommerce.apps.products.models.attribute_value import AttributeValue
from drfecommerce.apps.products.models.product_line import ProductLine


class ProductLineAttributeValue(models.Model):
    attribute_value = models.ForeignKey(to=AttributeValue, on_delete=models.CASCADE, related_name='attribute_values_av')
    product_line = models.ForeignKey(to=ProductLine, on_delete=models.CASCADE, related_name='attribute_values_pl')

    class Meta:
        unique_together = ('attribute_value', 'product_line')
        verbose_name = 'Product Line Attribute Value'
        verbose_name_plural = 'Product Line Attribute Values'

    def clean(self):
        queryset = (
            ProductLineAttributeValue.objects.filter(attribute_value=self.attribute_value)
            .filter(product_line=self.product_line)
            .exists()
        )

        if not queryset:
            iqs = Attribute.objects.filter(attribute_values__product_lines=self.product_line).values_list(
                'pk', flat=True
            )

            if self.attribute_value.attribute.id in list(iqs):
                raise ValidationError("Duplicate attribute exists")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductLineAttributeValue, self).save(*args, **kwargs)
