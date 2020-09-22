from django.contrib import admin
from home.models import Service, Category, ConcreteProduct


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'service_id')


class ConcreteProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'category_id', 'service_id')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ConcreteProduct, ConcreteProductAdmin)
