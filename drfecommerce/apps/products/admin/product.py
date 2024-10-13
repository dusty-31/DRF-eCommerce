from django.contrib import admin

from drfecommerce.apps.products.admin.inlines.product_line import ProductLineInline
from drfecommerce.apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description',
        'is_digital',
        'brand',
        'category',
        'is_active',
    ]
    inlines = [
        ProductLineInline,
    ]
