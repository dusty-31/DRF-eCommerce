from django.contrib import admin

from drfecommerce.apps.products.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
