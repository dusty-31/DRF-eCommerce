from django.core import checks
from django.db import models


class OrderField(models.PositiveIntegerField):
    description = 'Ordering field on a unique field.'

    def __init__(self, unique_for_fields=None, *args, **kwargs):
        self.unique_for_fields = unique_for_fields
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_unique_for_fields_attribute(**kwargs),
        ]

    def _check_unique_for_fields_attribute(self, **kwargs):
        if self.unique_for_fields is None:
            return [
                checks.Error(
                    'OrderField must define a \'unique_for_fields\' attribute.',
                )
            ]
        elif self.unique_for_fields not in [field.name for field in self.model._meta.get_fields()]:
            return [
                checks.Error(
                    'OrderField  \'unique_for_fields\' attribute must be a valid field on the model.',
                )
            ]
        return []

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                queryset = self.model.objects.all()
                if self.unique_for_fields:
                    queryset = queryset.filter(
                        **{self.unique_for_fields: getattr(model_instance, self.unique_for_fields)}
                    )
                last_item = queryset.latest(self.attname)
                value = last_item.order + 1
            except self.model.DoesNotExist:
                value = 1  # first item
            setattr(model_instance, self.attname, value)
            return value
