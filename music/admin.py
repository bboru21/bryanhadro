from django.contrib import admin

from .models import (
    Artist,
    Category,
    Song,
)

from .forms import (
    ArtistAdminForm,
)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    form = ArtistAdminForm

    readonly_fields = ('sort_name',)
    ordering = ('sort_name',)
    list_display = ('name', 'sort_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'primary',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    fields = ('name', 'artist', 'categories', 'youtube_video_link',)
    list_display = ('name', 'artist',)
    list_filter = ('categories',)

