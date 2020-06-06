from django.db import models

from core.constants import CLOTHES, SERVICE


class ProductServiceBase(models.Model):

    name = models.CharField(max_length=300, blank=False)
    price = models.IntegerField(blank=False)
    description = models.TextField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}: {self.price}'


class Product(ProductServiceBase):
    size = models.IntegerField()
    type = models.PositiveSmallIntegerField(choices=CLOTHES)
    existence = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Service(ProductServiceBase):
    approximate_duration = models.IntegerField(blank=True)
    service_type = models.PositiveSmallIntegerField(choices=SERVICE)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Service'
