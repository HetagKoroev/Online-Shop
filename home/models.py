from django.db import models


class Service(models.Model):
    """ Примеры: Инстаграм, Вконтакте, Youtube и т.п. """
    service = models.CharField(default='Разное', max_length=15, blank=False, null=False)

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"

    def __repr__(self):
        return self.service

    def __str__(self):
        return self.service


class Category(models.Model):
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(default='Разное', max_length=10)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=40, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    description = models.TextField(blank=False, null=True)

    class Meta:
        abstract = True
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class ConcreteProduct(Product):
    pass
