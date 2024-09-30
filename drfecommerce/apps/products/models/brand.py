from django.db import models

from drfecommerce.apps.products.managers import ActiveManager


class Brand(models.Model):
    name = models.CharField(max_length=120, unique=True)
    is_active = models.BooleanField(default=False)

    objects = models.Manager()
    active_objects = ActiveManager()

    def __str__(self) -> str:
        return self.name
