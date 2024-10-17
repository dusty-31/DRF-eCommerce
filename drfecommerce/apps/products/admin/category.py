from django.contrib import admin

from drfecommerce.apps.products.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = [
        'slug',
    ]
