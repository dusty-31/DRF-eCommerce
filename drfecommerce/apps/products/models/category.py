from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from drfecommerce.apps.products.managers import ActiveManager


class Category(MPTTModel):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    is_active = models.BooleanField(default=False)
    parent = TreeForeignKey(to='self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')

    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        verbose_name_plural = 'Categories'

    class MPPTMeta:
        order_insertion_by = ['name']

    def __str__(self) -> str:
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        self.slug = self.name.replace(' ', '-').lower()
        super().save()
