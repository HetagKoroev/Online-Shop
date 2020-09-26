from django.contrib import admin
from home.models import Service, Category, ConcreteProduct


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'service_id')


@admin.register(ConcreteProduct)
class ConcreteProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'category_id', 'service_id')
