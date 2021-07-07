from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']


class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        null=True,
    )
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ['artist', 'name']
