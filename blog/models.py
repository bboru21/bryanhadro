from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):

    title = models.CharField(max_length=255, null=False)
    urlname = models.URLField(db_column='urlname', null=False, unique=True)
    content = RichTextUploadingField(config_name='default', null=True)
    created_date = models.DateTimeField(null=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        # db_table = 'blog_post'
        pass

    def __str__(self):
        return f'{self.title} ({self.pk})'
