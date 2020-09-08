from django.db import models


class Category(models.Model):
    category = models.CharField(default='Разное', max_length=15, blank=False, null=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __repr__(self):
        return self.category

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Instagram(Product):
    class Meta:
        verbose_name = "Инстраграм"
        verbose_name_plural = "Инстраграм"
