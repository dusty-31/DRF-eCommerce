from django.contrib import admin

from drfecommerce.apps.products.admin.inlines.attribute_value_product import AttributeValueProductInline
from drfecommerce.apps.products.admin.inlines.product_line import ProductLineInline
from drfecommerce.apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description',
        'is_digital',
        'category',
        'is_active',
        'product_type',
    ]
    inlines = [
        ProductLineInline,
        AttributeValueProductInline,
    ]
