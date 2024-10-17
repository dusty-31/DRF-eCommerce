from django.contrib import admin

from drfecommerce.apps.products.models import Attribute


class AttributeInline(admin.TabularInline):
    model = Attribute.product_type_attribute.through
