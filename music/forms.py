import re

from django import forms

from .models import (
    Artist,
    Song,
)

class ArtistAdminForm(forms.ModelForm):

    def save(self, commit=True):
        instance = super(ArtistAdminForm, self).save(commit=False)

        # save sort_name as Beatles, The
        sort_name = self.cleaned_data.get('name')
        m = re.match('The ', sort_name)
        if m:
            sort_name = '{}, {}'.format(
                sort_name[m.end():],
                sort_name[m.start():m.end()-1],
            )
        instance.sort_name = sort_name

        if commit:
            instance.save()
            # self.save_m2m()
        return instance

    class Meta:
        model = Artist
        fields = ('name','sort_name',)


class SongAdminForm(forms.ModelForm):

    def clean(self):

        # validate song name and artist are unique
        name = self.cleaned_data.get('name')
        artist = self.cleaned_data.get('artist')

        if Song.objects.filter(name=name, artist__name=artist.name).count() > 0:
            raise forms.ValidationError("Song and Artist already exist.")

    class Meta:
        model = Song
        fields = ('name', 'artist', 'categories', 'youtube_video_link',)
