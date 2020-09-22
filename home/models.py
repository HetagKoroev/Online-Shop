from django.db import models


class Service(models.Model):
    """ Инстаграм; Вконтакте; Youtube и т.п. """
    name = models.CharField(verbose_name=u'Наименование', default='Разное', max_length=15, blank=False, null=False)

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __repr__(self):
        return self.name

    def __str__(self):
        return str(self.id)


class Category(models.Model):
    """ Подписчики; Лайки; Просмотры и т.п. """
    service_id = models.ForeignKey(Service, verbose_name=u'Сервис', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Наименование', default='Разное', max_length=10)
    description = models.TextField(verbose_name=u'Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __repr__(self):
        return self.name

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    """ 100 мгновенных подписчиков; 1000 лайков; 1000 просмотров и т.п. """
    category_id = models.ForeignKey(Category, verbose_name=u'Категория', on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, verbose_name=u'Сервис', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Наименование', default='', max_length=40, blank=False, null=False)
    price = models.FloatField(verbose_name=u'Цена', blank=False, null=False)
    description = models.TextField(verbose_name=u'Описание', blank=False, null=True)

    class Meta:
        abstract = True
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __repr__(self):
        return f'{self.name} {self.service_id}'

    def __str__(self):
        return f'{self.name} {self.service_id}'


class ConcreteProduct(Product):
    pass
