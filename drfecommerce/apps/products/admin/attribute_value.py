from django.contrib import admin

from drfecommerce.apps.products.models import AttributeValue


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    pass
