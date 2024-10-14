from django.contrib import admin

from drfecommerce.apps.products.admin.inlines import AttributeValueInline, ProductImageInline
from drfecommerce.apps.products.models import ProductLine


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        AttributeValueInline,
    ]
