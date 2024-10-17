from django.core.exceptions import ValidationError
from django.db import models

from drfecommerce.apps.products.fields import OrderField
from drfecommerce.apps.products.managers import ActiveManager
from drfecommerce.apps.products.models import Product


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='product_lines')
    order = OrderField(unique_for_field='product', blank=True)
    is_active = models.BooleanField(default=True)
    attribute_values = models.ManyToManyField(
        to='AttributeValue',
        through='ProductLineAttributeValue',
        related_name='product_lines',
    )

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self) -> str:
        return f'Name: {self.product.name} | SKU: {self.sku}'

    def clean(self):
        queryset = ProductLine.objects.filter(product=self.product)
        for obj in queryset:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError('Order must be unique for each product.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductLine, self).save(*args, **kwargs)
