from django.db import models

from drfecommerce.apps.products.fields import OrderField
from drfecommerce.apps.products.models.product_line import ProductLine


class ProductImage(models.Model):
    alternative_text = models.CharField(max_length=120, blank=True)
    url = models.ImageField(upload_to='products_images/', default='/images/default.jpg')
    product_line = models.ForeignKey(to=ProductLine, on_delete=models.CASCADE, related_name='product_images')
    order = OrderField(unique_for_field='product_line', blank=True)

    def __str__(self):
        return f'Product Line: {self.product_line.sku} | Name: {self.url}'
