from django.contrib import admin

from drfecommerce.apps.products.models import Attribute


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass
