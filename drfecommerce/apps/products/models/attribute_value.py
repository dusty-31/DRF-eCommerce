from django.db import models


class AttributeValue(models.Model):
    value = models.CharField(max_length=120)
    attribute = models.ForeignKey('Attribute', on_delete=models.CASCADE, related_name='attribute_values')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Attribute Value'
        verbose_name_plural = 'Attribute Values'
