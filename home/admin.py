from django.contrib import admin
from home.models import Service, Category, ConcreteProduct


class ServiceAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class ConcreteProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ConcreteProduct, ConcreteProductAdmin)
