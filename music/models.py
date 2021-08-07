from django.db import models


_MAX_URL_LENGTH = 2048


class Artist(models.Model):
    name = models.CharField(max_length=255)
    sort_name = models.CharField(
        max_length=255,
        null=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.sort_name


class Category(models.Model):
    name = models.CharField(max_length=255)
    primary = models.BooleanField(default=False)

    class Meta:
        ordering = ['-primary', 'name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        null=True,
        related_name='songs',

    )
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='songs',
    )
    youtube_video_link = models.URLField(
        max_length=_MAX_URL_LENGTH,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['artist', 'name']

    def __str__(self):
        return self.name
