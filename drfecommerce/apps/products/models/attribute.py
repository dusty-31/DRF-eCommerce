from django.db import models


class Attribute(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
