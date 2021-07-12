from django.conf import settings
from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to=settings.IMAGES_URL[1:]) # ignore leading slash
    alt = models.CharField(max_length=255)
    caption = models.TextField()
