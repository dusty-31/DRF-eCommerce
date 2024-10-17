from django.contrib import admin

from drfecommerce.apps.products.models import AttributeValue


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue.product_lines.through
