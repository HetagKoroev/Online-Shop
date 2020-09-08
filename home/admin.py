from django.contrib import admin
from home.models import Instagram


class InstagramAdmin(admin.ModelAdmin):
    pass


admin.site.register(Instagram, InstagramAdmin)
