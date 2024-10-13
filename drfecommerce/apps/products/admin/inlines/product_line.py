from django.contrib import admin

from drfecommerce.apps.products.models import ProductLine

from .edit_link import EditLinkInline


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    extra = 0
    readonly_fields = [
        'edit',
    ]
