from django.contrib import admin
from home.models import Category, Instagram


class InstagramAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Instagram, InstagramAdmin)
admin.site.register(Category, CategoryAdmin)
