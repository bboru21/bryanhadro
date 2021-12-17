from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField


class PostCategory(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255, null=False)
    urlname = models.URLField(db_column='urlname', null=False, unique=True)
    content = RichTextUploadingField(config_name='blogContent', null=True)
    created_date = models.DateTimeField(null=True)
    modified_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(
        PostCategory,
        blank=True,
        default=None,
        related_name='posts',
    )
    active = models.BooleanField(default=True)

    class Meta:
        # db_table = 'blog_post'
        ordering = ('-created_date',)

    def __str__(self):
        return f'{self.title} ({self.pk})'

    @property
    def url(self):
        return reverse('blog_post', kwargs={
            'year': self.created_date.strftime('%Y'),
            'month': self.created_date.strftime('%m'),
            'day': self.created_date.strftime('%d'),
            'urlname': self.urlname,
        })



