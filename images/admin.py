from django.contrib import admin

from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('file', 'name', 'alt', 'caption',)
