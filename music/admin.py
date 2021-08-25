from django.contrib import admin

from .models import (
    Artist,
    Category,
    Song,
)

from .forms import (
    ArtistAdminForm,
    SongAdminForm,
)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    form = ArtistAdminForm

    readonly_fields = ('sort_name',)
    ordering = ('sort_name',)
    list_display = ('name', 'sort_name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'primary',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    form = SongAdminForm
    list_display = ('name', 'artist',)
    list_filter = ('categories',)
    autocomplete_fields = ('artist',)
    search_fields = ('name', 'artist__name',)

