from django.contrib import admin

from drfecommerce.apps.products.models import AttributeValue


class AttributeValueProductInline(admin.TabularInline):
    model = AttributeValue.product_attr_value.through
