from django.contrib import admin
from home.models import Platform, Category, ConcreteService


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'platform_id')


@admin.register(ConcreteService)
class ConcreteServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'category_id', 'platform_id')
