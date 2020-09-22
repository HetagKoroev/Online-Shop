from django.contrib import admin
from home.models import Service, Category, ConcreteProduct


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class ConcreteProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ConcreteProduct, ConcreteProductAdmin)
