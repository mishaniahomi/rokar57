from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'href', 'prewiew')
    list_display_links = ('id', 'title', 'description', 'created_at', 'href', 'prewiew')
    search_fields = ('id', 'title', 'description', 'created_at', 'href')

    def prewiew(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-width: 70%;">')

