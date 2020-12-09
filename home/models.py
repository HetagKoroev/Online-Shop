from django.db import models


class Platform(models.Model):
    """ Инстаграм; Вконтакте; Youtube и т.п. """
    name = models.CharField(verbose_name=u'Наименование', default='Разное', max_length=15, blank=False, null=False)

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'

    def __str__(self):
        return self.name


class Category(models.Model):
    """ Подписчики; Лайки; Просмотры и т.п. """
    platform_id = models.ForeignKey(Platform, verbose_name=u'Платформа', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Наименование', default='Разное', max_length=10)
    description = models.TextField(verbose_name=u'Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} {self.platform_id}'


class Service(models.Model):
    """ 100 мгновенных подписчиков; 1000 лайков; 1000 просмотров и т.п. """
    category_id = models.ForeignKey(Category, verbose_name=u'Категория', on_delete=models.CASCADE)
    platform_id = models.ForeignKey(Platform, verbose_name=u'Платформа', on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'Наименование', default='', max_length=40, blank=False, null=False)
    price = models.FloatField(verbose_name=u'Цена')
    description = models.TextField(verbose_name=u'Описание')
    api_id = models.CharField(verbose_name=u'ID сервиса', unique=True, max_length=40, null=False, blank=False)

    class Meta:
        abstract = True
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __str__(self):
        return f'{self.name} {self.platform_id}'


class ConcreteService(Service):
    pass
