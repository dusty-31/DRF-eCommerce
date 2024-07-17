from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from drfecommerce.apps.products.models import Brand, Category, Product, ProductImage, ProductLine


class EditLinkInline(object):
    def edit(self, instance):
        url = reverse(
            f'admin:{instance._meta.app_label}_{instance._meta.model_name}_change',
            args=[instance.pk],
        )
        if instance.pk:
            link = mark_safe(f'<a href="{url}">Edit</a>')
            return link
        else:
            return ''


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    extra = 0
    readonly_fields = [
        'edit',
    ]


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
        ProductLineInline,
    ]


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
