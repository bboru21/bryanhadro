from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# width, height
# 3:2 aspect ratio
_DIMENSIONS = {
    'thumbnail': (90, 60),
    'small': (300, 200),
    'medium': (600, 400),
    'large': (1200, 800),
}

_UPLOAD_DIR = f'{settings.IMAGES_URL[1:]}uploads/' # ignore leading slash

class Image(models.Model):
    file = models.ImageField(upload_to=_UPLOAD_DIR)
    file_thumbnail = ImageSpecField(
        source='file',
        processors=[ResizeToFill(
            _DIMENSIONS['thumbnail'][0],
            _DIMENSIONS['thumbnail'][1],
        )],
        format='JPEG',
        options={'quality': 80},
    )
    file_small = ImageSpecField(
        source='file',
        processors=[ResizeToFill(
            _DIMENSIONS['small'][0],
            _DIMENSIONS['small'][1],
        )],
        format='JPEG',
        options={'quality': 80},
    )
    file_medium = ImageSpecField(
        source='file',
        processors=[ResizeToFill(
            _DIMENSIONS['medium'][0],
            _DIMENSIONS['medium'][1],
        )],
        format='JPEG',
        options={'quality': 80},
    )
    file_large = ImageSpecField(
        source='file',
        processors=[ResizeToFill(
            _DIMENSIONS['large'][0],
            _DIMENSIONS['large'][1],
        )],
        format='JPEG',
        options={'quality': 80},
    )
    name = models.CharField(max_length=255, null=True)
    alt = models.CharField(max_length=255)
    caption = models.TextField()

    def __str__(self):
        return self.name
