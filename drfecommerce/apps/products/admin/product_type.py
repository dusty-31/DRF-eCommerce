from django.contrib import admin

from drfecommerce.apps.products.admin.inlines import AttributeInline
from drfecommerce.apps.products.models import ProductType


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        AttributeInline,
    ]
