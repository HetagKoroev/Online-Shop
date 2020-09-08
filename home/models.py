from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=15, blank=False, null=False)


class Product(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        abstract = True
