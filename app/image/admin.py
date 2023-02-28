from django.contrib import admin
from .models import Image, Thumbnail


class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "author"]

admin.site.register(Image, imageAdmin)
admin.site.register(Thumbnail)