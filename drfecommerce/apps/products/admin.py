from django.contrib import admin

from drfecommerce.apps.products.models import Brand, Category, Product, ProductLine


class ProductLineInLine(admin.TabularInline):
    model = ProductLine
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = [
        'slug',
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description',
        'is_digital',
        'brand',
        'category',
        'is_active',
    ]
    inlines = [
        ProductLineInLine,
    ]


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    pass
