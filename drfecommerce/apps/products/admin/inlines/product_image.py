from django.contrib import admin

from drfecommerce.apps.products.models import ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
