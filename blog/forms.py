from django import forms
from django.utils.text import slugify

from .models import Post

class PostForm(forms.ModelForm):
    model = Post
    fields = ('title', 'content', 'urlname',)

    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=False)

        if not instance.urlname:
            urlname = slugify(instance.title)
            # if Post.objects.filter(urlname==urlname).count() > 0:
            #     # TODO make unique
            #     pass

            instance.urlname = urlname

        if commit:
            instance.save()

        return instance