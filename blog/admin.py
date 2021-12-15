from django.contrib import admin

from .models import ( Post, PostCategory )
from .forms import PostForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    readonly_fields = ('urlname',)
    autocomplete_fields = ('categories',)

    fields = ('title', 'content', 'created_date', 'urlname', 'categories', 'active',)


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
