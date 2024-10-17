from django.db import models


class ProductTypeAttribute(models.Model):
    product_type = models.ForeignKey(
        'ProductType',
        on_delete=models.CASCADE,
        related_name='product_type_attributes',
    )
    attribute = models.ForeignKey(
        'Attribute',
        on_delete=models.CASCADE,
        related_name='product_type_attributes',
    )

    class Meta:
        unique_together = ('product_type', 'attribute')

    def __str__(self):
        return f'{self.product_type.name} - {self.attribute.name}'
