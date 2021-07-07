from django.contrib import admin

from .models import (
    Artist,
    Category,
    Song,
)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    fields = ('name', 'artist', 'categories', 'youtube_video_link',)

